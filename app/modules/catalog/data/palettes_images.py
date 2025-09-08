# app/modules/catalog/data/palette_images.py

from __future__ import annotations

# Provide the 6 swatch URLs per palette group in order → I, II, III, IV, V, VI
PALETTE_URLS: dict[str, list[str]] = {
    "Marine Dusk": [
        "https://api.renoworks.com/v1/palette/fd9abdb9-0ce2-41de-ba14-0007ed023963/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/16cec50d-5da6-43c7-a309-35131cd01ccf/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/2e74fed8-872f-4623-b53b-a8e5fcd517f2/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/642bd73a-ec72-4fe0-82ac-08e783845e95/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/42eade81-44d9-4bde-b2f7-71c853d2575d/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/0330ea25-ffc7-42da-9eef-5f401c3f2d8b/image?global=true&site=gentekcanada",
    ],
    "Chesapeake Gray": [
        "https://api.renoworks.com/v1/palette/da86c537-ddfb-4c3c-be52-be4cd2860e9f/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/5370a27e-ce02-433b-a456-f062254451ed/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/7f1bb175-b7f2-44b0-8e65-f92a7b69223a/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/f50726e8-c77b-4215-95f5-395e0d5b20a6/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/eb840625-3d43-4875-b946-240b7767be76/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/ae001e9f-bf71-4b6c-9d30-bc944a704031/image?global=true&site=gentekcanada",
    ],
    "Majestic Brick": [
        "https://api.renoworks.com/v1/palette/00ab26be-aba0-4634-93f9-6d30971428b6/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/dad64ffb-0518-4af1-a607-0b995e6ee34d/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/b3b94786-c2d5-4c23-8312-2122ee7d8651/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/456520cd-4372-4dad-ae18-a9f279174994/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/156c51bf-4253-47fd-8e67-bc982757e8fa/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/fa6ef348-4339-4662-8ab8-427a34e56f7c/image?global=true&site=gentekcanada",
    ],
    "Rockport Brown": [
        "https://api.renoworks.com/v1/palette/19204d00-20b8-4d6e-8e92-e98730bfa585/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/df52768d-eeeb-4faa-835f-4bd5fb1e3ece/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/ca0f61d2-700e-49be-b4d6-906ad1a26a9b/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/b4a4fa22-9ad7-4a89-8955-9661c44631c2/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/e80c48c1-98f0-4625-92a6-254fb430c809/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/a7050430-1ade-48c9-873b-9099ea1f9064/image?global=true&site=gentekcanada",
    ],
    "Smoked Timber": [
        "https://api.renoworks.com/v1/palette/4f7cc4c5-0cbb-453a-a3f6-7595b7e2f4c1/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/7b3f3369-dc03-4533-9d74-1b0bd8797968/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/fa6c3ab7-55ca-4e48-87d7-712a13846fac/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/e6eb6102-178a-44ef-818c-3231b9afc733/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/a9f48eee-4b1e-420a-899b-69320bdc056d/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/33b238b6-b2c7-49ee-9ca2-8821dc655db9/image?global=true&site=gentekcanada",
    ],
    "Meadow Fern": [
        "https://api.renoworks.com/v1/palette/6f705158-91c6-44d4-b7a6-ba597211a00d/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d4e04db2-7004-4e98-8f67-a5f7343dc40e/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/b6b1f36a-342a-49f6-8e45-d5a352a44882/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/a03ed15a-e06b-44b7-b2e4-231fdb746f5e/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/da458d80-9773-4765-8e6d-ac0749523df0/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/84a6f2a2-0a14-4e15-9f78-0735330313d8/image?global=true&site=gentekcanada",
    ],
    "Hudson Slate": [
        "https://api.renoworks.com/v1/palette/b095eda8-d0ae-4677-8386-3ef7042b3b98/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/dece4018-b44f-4cf0-bac4-4325e106c1fd/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/1fdca401-a6ec-460a-b667-db2fe6a1e56b/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/0c15735b-8f57-4f71-b130-3e7bd3c50d4b/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/62f00bd4-4f14-4a09-8ad4-467556a15d94/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/471d4b84-0930-47ac-a2a3-87b1f0aecd4e/image?global=true&site=gentekcanada",
    ],
    "Rockwell Blue": [
        "https://api.renoworks.com/v1/palette/57cc1c06-3816-424a-94ed-ac79028f47a7/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/5124061c-9ad7-48f3-bf32-d007bcd3f103/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/1de5bd55-e506-480f-836a-6587c0f261e1/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/64b42422-61ba-4b31-867d-32f17f00a072/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/b15bd451-9d69-4b47-a024-e0bf2eadd588/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/83106f20-3c60-4beb-8194-07ebb4e66026/image?global=true&site=gentekcanada",
    ],
    "Monterey Sand": [
        "https://api.renoworks.com/v1/palette/216f227b-5dd0-4a1f-a586-2dfcbffed95d/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/91d2edae-d50f-41eb-ad13-63a462e3da2d/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/c1600c5d-fe9e-4e78-988f-bb5591cd7454/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/db44d334-3901-4732-80cc-902fb3e16456/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/55781cbe-a062-4912-9db3-ce575188bf76/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/2c1210a6-2d4a-4e86-a201-7b9b8c1fc0c4/image?global=true&site=gentekcanada",
    ],
    "Dover Gray": [
        "https://api.renoworks.com/v1/palette/0392a930-c071-4bcf-b78c-086ec86fa255/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/2b6312ae-d2a4-4247-a39a-efea92fb1041/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/f62636f5-f2a7-4c4b-8236-93d488fa58cf/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/5928dfa5-6523-45a6-84ed-6077a0cc5e3f/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/ac67c2e4-faff-4d47-aa9d-fd5a01367b2b/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/46de1fb6-3bb0-4c04-bfde-06a23491d1d3/image?global=true&site=gentekcanada",
    ],
    "Wicker": [
        "https://api.renoworks.com/v1/palette/8a6ec716-b6e1-4d37-8675-adccbc124f54/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d4fae1cf-fda4-4c1b-9c27-c77d2c81d6c4/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/a360eb69-643d-4b0b-843e-a3f942bb8dcc/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/e091dd86-6929-4d83-9bdc-f77e11f87496/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d9b37da6-de75-42b5-8b7c-305d493edd47/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/ffddc9b2-0e12-4659-9d1c-694642b69178/image?global=true&site=gentekcanada",
    ],
    "Midnight Surf": [
        "https://api.renoworks.com/v1/palette/790f6fe8-539c-4f76-bf3e-f67a637cc16b/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/377449c0-0dea-4ced-bd26-b1601648bba1/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d85d0eac-b977-4198-b228-3ac51c5a3624/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/1604d0fc-9092-4b45-a471-ff4ac7e2fa81/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/09e54c83-0d26-46af-832e-72109a6b74fe/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/50e36ed9-0da0-47b5-bf89-8c3d403bde3a/image?global=true&site=gentekcanada",
    ],
    "Pearl": [
        "https://api.renoworks.com/v1/palette/e95992fa-de71-4b94-8756-3a13b9aa54c3/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/2fea0ec5-07ca-4808-8366-ffd56efe5466/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/402a3fb0-b1a1-4a73-bf28-d9174a06755c/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/90180a2a-a251-4da2-af6f-0024e7f54ada/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/999a5bff-5190-4f0d-98c5-4fe6cf9b36ed/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/8f3b7788-3c95-4c34-bcf0-a846004aa7ee/image?global=true&site=gentekcanada",
    ],
    "Dark Drift": [
        "https://api.renoworks.com/v1/palette/180c882d-0016-4253-b53d-654e1f8be1cb/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/544bd6c8-63c0-4313-ab69-09c99fe47077/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/93b715c4-9e72-4922-b6da-47d0eabfb2c3/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/139a9289-f76a-461f-837a-22b5f9f74b22/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/a919645a-3d0a-43fb-9e51-e846cdde9522/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/f5199032-ce6d-41b3-8376-0fc31f4ca41c/image?global=true&site=gentekcanada",
    ],
    "Juniper Grove": [
        "https://api.renoworks.com/v1/palette/d8990692-6d13-41ca-bc15-51f1e76ba7bb/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/249df640-00dd-4239-a033-f5d2b2f0e7d7/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/64bb3d87-6c06-4c48-af20-8494e6fcec73/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/4de13fd3-c47b-4482-9a23-35a9e2459e05/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/922cfa11-b169-4b78-a569-6fd4c15a9035/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/20d6b657-2c81-47cf-9709-8c49427d5c75/image?global=true&site=gentekcanada",
    ],
    "Espresso": [
        "https://api.renoworks.com/v1/palette/6e224222-7e3a-4e81-8e7c-ca27ab33b45e/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/cbbddef2-edab-42d3-b14a-162a3bb1a156/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/be529a12-68bd-4cc7-946b-307897b793fe/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/c75931b6-3db6-4bf7-abf1-a7ce6765a696/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/a631d203-e0e8-4e10-a826-25e17fc6fb50/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/4542477c-d501-484f-acf1-345654fe16c6/image?global=true&site=gentekcanada",
    ],
    "Windswept Smoke": [
        "https://api.renoworks.com/v1/palette/563c6051-562c-4cc4-b328-e9db83d89906/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/1d9af523-a708-4ab8-8b13-89652be8cb81/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/b1e210d5-aea2-4370-9088-f730d1238018/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/ed5d4ef3-2afa-430e-ad15-8ab617911d97/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/f7dca505-4a2d-4e38-bc40-d4326edac6ba/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/1f8542ed-dd1c-464a-9229-e1ee1ce85feb/image?global=true&site=gentekcanada",
    ],
    "Moonlit Moss": [
        "https://api.renoworks.com/v1/palette/3fc04fee-24cf-44b2-b547-6bdd0acb88df/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/5c3ad912-aa8b-4ada-bea7-00a062ee377e/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d937f0c8-2bf7-44e5-b837-4fe3ad6fd1fd/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/ad6a7372-fbeb-4731-a13d-8a72ec19d1e4/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/34210cdf-2102-4111-978a-6b6240693b53/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/5792431c-3ef2-4b25-a076-b539c9d48733/image?global=true&site=gentekcanada",
    ],
    "Coastal Blue": [
        "https://api.renoworks.com/v1/palette/ab5d18f9-6b6b-4378-a549-e7acedab4e0e/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/78877286-b309-498f-8da3-ced4c1d87fb7/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/adac0d65-1b7a-47da-84a7-80efa4705202/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/96a04284-886c-4f31-959c-bbaae2cfa80a/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/2e6b89b4-ff08-4661-91a0-7452af551fed/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/2a59afd7-6347-468a-9acd-c232ae0a62d5/image?global=true&site=gentekcanada",
    ],
    "Pebble": [
        "https://api.renoworks.com/v1/palette/0d1472fc-35a9-45f4-9df4-1c90f474ae5a/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/c2612d7c-04c1-4b5a-9706-51f9b9f2e8b7/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/1f9ab433-23b9-4d2b-b415-74f2812142b9/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/86105a5d-e53c-45f9-837c-5a43b68dbc44/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/3258a1e3-96f0-43f8-be5f-14d265cb5124/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/06e987b0-30c6-4db5-bce1-32e9ad099809/image?global=true&site=gentekcanada",
    ],
    "Storm": [
        "https://api.renoworks.com/v1/palette/e4940774-3471-4c9c-b06f-58b910c53d97/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/f558dc01-8703-4a8c-9e2a-848618199ca8/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d922a912-c033-47cf-939c-c6a79842a9be/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/4105a5b1-0fdd-4026-9832-a9ebf4dad30d/image?global=true&site=gentekcanada",
    ],
    "Iron Ore": [
        "https://api.renoworks.com/v1/palette/0952816c-57fc-4df6-be9d-d0359fe2ecfd/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/5dd764e6-50e7-4892-bc9e-d4c698b230cf/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/50fed77e-5a5f-4b57-a985-0e60eeba15aa/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/aed82a0a-5680-44a6-bcf5-8661c8b0aac8/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/36d8dbea-9594-43f5-960b-23a3aaa6f000/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/48f35d63-852e-4773-8186-3b3192345fdb/image?global=true&site=gentekcanada",
    ],
    "Linen": [
        "https://api.renoworks.com/v1/palette/9358a6b8-51fa-4584-9b8c-4ef5beb0c5a0/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/254d3280-0e3c-4fec-8d0d-37f3f5ce512a/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/d910191a-dca1-4ec4-8333-ec808f41e393/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/0fd1c705-edc5-4cbe-86cf-2bea19360bda/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/c829b678-dba1-4d1f-bb7e-a339195dbaa9/image?global=true&site=gentekcanada",
        "https://api.renoworks.com/v1/palette/92b2e08f-378d-46e9-8af7-9a110c47334c/image?global=true&site=gentekcanada",
    ],
}

# Build the final map the controller will use.
# Keys must match your palette browsing paths, e.g.:
#   Palettes/<Group>/<Group> I … Palettes/<Group>/<Group> VI
_ROMAN = ["I", "II", "III", "IV", "V", "VI"]

PALETTE_IMAGE_MAP: dict[str, str] = {}

for group, urls in PALETTE_URLS.items():
    # optional: group tile image (first swatch)
    if urls:
        PALETTE_IMAGE_MAP[f"Palettes/{group}"] = urls[0]
    # item images
    for i, url in enumerate(urls[:6]):
        PALETTE_IMAGE_MAP[f"Palettes/{group}/{group} {_ROMAN[i]}"] = url
