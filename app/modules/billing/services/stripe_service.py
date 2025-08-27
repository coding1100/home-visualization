from __future__ import annotations
import stripe
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.core.config import settings
from app.modules.billing.models.payment import Payment
from app.modules.signupflow.models.user import User

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeService:
    def __init__(self, db: AsyncSession):
        self.db = db

    # ---- helpers ----
    async def _find_payment_by_any(self, *, checkout_session_id: str | None = None, payment_intent_id: str | None = None) -> Payment | None:
        stmt = select(Payment)
        if checkout_session_id:
            stmt = stmt.where(Payment.stripe_checkout_session_id == checkout_session_id)
        if payment_intent_id:
            stmt = stmt.where(Payment.stripe_payment_intent_id == payment_intent_id)
        return await self.db.scalar(stmt)

    async def ensure_customer_for_user(self, user: User) -> str | None:
        if not settings.STRIPE_SECRET_KEY:
            return None
        if user.stripe_customer_id:
            return user.stripe_customer_id
        # create customer
        customer = stripe.Customer.create(email=user.email, name=user.full_name or None)
        user.stripe_customer_id = customer["id"]
        await self.db.commit()
        return user.stripe_customer_id

    # ---- upserts from Stripe objects ----
    async def upsert_from_checkout_session(self, session: dict, user: User | None = None) -> Payment:
        # session is a stripe.checkout.Session
        pi = session.get("payment_intent")
        cus = session.get("customer")
        amount = session.get("amount_total")
        currency = session.get("currency")
        status = session.get("payment_status")  # 'paid' -> map to 'succeeded'
        status_map = {"paid": "succeeded", "unpaid": "requires_payment_method"}
        mapped_status = status_map.get(status, status or "created")

        existing = await self._find_payment_by_any(checkout_session_id=session["id"])
        if existing:
            existing.status = mapped_status
            existing.amount = amount
            existing.currency = currency
            existing.stripe_payment_intent_id = pi or existing.stripe_payment_intent_id
            existing.stripe_customer_id = cus or existing.stripe_customer_id
            if user and not existing.user_id:
                existing.user_id = user.id
            existing.raw = session
            await self.db.commit()
            await self.db.refresh(existing)
            return existing

        p = Payment(
            user_id=user.id if user else None,
            stripe_checkout_session_id=session["id"],
            stripe_payment_intent_id=pi,
            stripe_customer_id=cus,
            amount=amount,
            currency=currency,
            status=mapped_status,
            raw=session
        )
        self.db.add(p)
        await self.db.commit()
        await self.db.refresh(p)
        return p

    async def upsert_from_payment_intent(self, intent: dict, user: User | None = None) -> Payment:
        cus = intent.get("customer")
        amount = intent.get("amount")
        currency = intent.get("currency")
        status = intent.get("status")  # 'succeeded' | 'processing' | 'requires_payment_method' | ...
        charge_id = None
        if intent.get("latest_charge"):
            charge_id = intent["latest_charge"]

        existing = await self._find_payment_by_any(payment_intent_id=intent["id"])
        if existing:
            existing.status = status
            existing.amount = amount
            existing.currency = currency
            existing.stripe_customer_id = cus or existing.stripe_customer_id
            existing.stripe_charge_id = charge_id or existing.stripe_charge_id
            if user and not existing.user_id:
                existing.user_id = user.id
            existing.raw = intent
            await self.db.commit()
            await self.db.refresh(existing)
            return existing

        p = Payment(
            user_id=user.id if user else None,
            stripe_payment_intent_id=intent["id"],
            stripe_customer_id=cus,
            stripe_charge_id=charge_id,
            amount=amount,
            currency=currency,
            status=status,
            raw=intent,
        )
        self.db.add(p)
        await self.db.commit()
        await self.db.refresh(p)
        return p
