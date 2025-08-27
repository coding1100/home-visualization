import uuid

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import stripe

from app.core.config import settings
from app.modules.deps import get_db, get_current_user
from app.modules.billing.schemas.payment_schema import LinkRequest, PaymentOut
from app.modules.billing.services.stripe_service import StripeService
from app.modules.signupflow.models.user import User

billing_router = APIRouter(prefix="/billing", tags=["billing"])

@billing_router.post("/link", response_model=PaymentOut)
async def link_payment(
    body: LinkRequest,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if not settings.STRIPE_SECRET_KEY:
        raise HTTPException(status_code=500, detail="Stripe not configured on backend")

    if not body.has_any:
        raise HTTPException(status_code=400, detail="Provide checkout_session_id or payment_intent_id")

    stripe.api_key = settings.STRIPE_SECRET_KEY
    svc = StripeService(db)

    try:
        if body.checkout_session_id:
            session = stripe.checkout.Session.retrieve(body.checkout_session_id)
            p = await svc.upsert_from_checkout_session(session, current_user)
            return p
        intent = stripe.PaymentIntent.retrieve(body.payment_intent_id)
        p = await svc.upsert_from_payment_intent(intent, current_user)
        return p
    except stripe.error.AuthenticationError:
        raise HTTPException(status_code=502, detail="Stripe auth failed (check STRIPE_SECRET_KEY)")
    except stripe.error.InvalidRequestError as e:
        raise HTTPException(status_code=400, detail=f"Stripe invalid request: {e.user_message or str(e)}")
    except Exception:
        raise HTTPException(status_code=502, detail="Stripe call failed")

@billing_router.post("/webhooks/stripe")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    raw_body: bytes = await request.body()
    sig = request.headers.get("Stripe-Signature")  # canonical
    if not settings.STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=500, detail="STRIPE_WEBHOOK_SECRET is not set")

    # (optional) set API key once here in case we ever fetch from Stripe in this path
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        # add tolerance to avoid clock drift issues (default ~300s)
        event = stripe.Webhook.construct_event(
            payload=raw_body,
            sig_header=sig,
            secret=settings.STRIPE_WEBHOOK_SECRET,
            # tolerance=300,  # uncomment if you want to override default
        )
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid payload")

    etype = event["type"]
    data = event["data"]["object"]

    # --- Optional debug logging ---
    try:
        print(f"[stripe] event {event['id']} type={etype} livemode={event.get('livemode')}")
    except Exception:
        pass

    svc = StripeService(db)
    user: User | None = None

    # Try to resolve user
    # 1) client_reference_id (we recommend FE sets this to the user's UUID)
    # 2) fallback: match by stripe_customer_id if present
    def resolve_user_by_client_ref(v: str | None):
        if not v:
            return None
        try:
            return uuid.UUID(str(v))
        except Exception:
            return None

    client_ref = None
    if etype.startswith("checkout.session"):
        client_ref = resolve_user_by_client_ref(data.get("client_reference_id"))
        if client_ref:
            user = await db.scalar(select(User).where(User.id == client_ref))
        if not user and data.get("customer"):
            user = await db.scalar(select(User).where(User.stripe_customer_id == data["customer"]))

        # Only update on meaningful states
        if etype == "checkout.session.completed":
            await svc.upsert_from_checkout_session(data, user)

    elif etype.startswith("payment_intent"):
        if data.get("customer"):
            user = await db.scalar(select(User).where(User.stripe_customer_id == data["customer"]))
        if etype == "payment_intent.succeeded":
            await svc.upsert_from_payment_intent(data, user)
        elif etype == "payment_intent.payment_failed":
            await svc.upsert_from_payment_intent(data, user)  # will store failed status too

    elif etype.startswith("charge.refunded"):
        # Optional: you can enrich the record on refunds if you want
        # intent_id = data.get("payment_intent")
        # p = await svc.upsert_from_payment_intent({'id': intent_id, ...}, user)
        pass

    # Always acknowledge so Stripe stops retrying
    return {"received": True}