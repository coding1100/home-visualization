# app/modules/catalog/data/product_images.py

PRODUCT_IMAGE_MAP: dict[str, str] = {
    # === Wall → Categories (you already tested these) ===
    # "Wall/categories/Brick":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2Flogo.png",
    # "Wall/categories/Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    # "Wall/categories/Stone":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2Flogo.png",

    # "Wall/categories/Premium Composite Siding":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    "Wall/Board and Batten":"https://res.cloudinary.com/x-nabeel-x/image/upload/v1758714944/users/a203d682-0b66-4b4a-949a-59fe6209cee9/562f7e31-0f70-46cc-847a-168a430ab96f_image_1_usvhtp.png",
    "Wall/Lap Siding":"https://res.cloudinary.com/x-nabeel-x/image/upload/v1758715074/users/a203d682-0b66-4b4a-949a-59fe6209cee9/6d59f056-d8ad-4c54-9982-df6a1d66d643_image_cs2rvi.png",


    "Wall/Lap Siding/Bourbon": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-112918_3c19677c-e3b6-4caa-b883-3aedb8be9760_bcb2483e-ba34-4ab8-bba4-e0ee00f9e7b2_Bourbon.png",
    "Wall/Lap Siding/Charcoal": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113302_e2198a68-4872-4ccc-8199-8fcce0e4ea92_1417c153-2f02-42b6-8012-83baf89d6e94_Charcoal.png",
    "Wall/Lap Siding/Khaki": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113548_d9f43607-dedf-4c5c-81c9-498b6c02d70d_d29a0b8b-4d62-48dd-8560-d08e29ddcf5e_Khaki.png",
    "Wall/Lap Siding/Midnight": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113728_4b3c51bc-358b-46dd-ba26-57bf25a4bc55_e93004fc-2417-49c6-99cf-8332ed4c179f_Midnight.png",
    "Wall/Lap Siding/Ocean Mist": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113917_fc518223-7680-4871-8eac-f7f8e48b3a21_44b395a0-894f-4681-9a3d-26eeea90d888_Ocean%20Mist.png",
    "Wall/Lap Siding/Polar White": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114106_71776c25-5c9a-401d-bff1-6d66adaebb59_97eff863-3dfa-4608-a347-d241580dcde8_Polar%20White.png",
    "Wall/Lap Siding/Saddle Brown": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114237_e65b535e-32a1-4735-bfe0-476366fab176_f488f99d-25d5-4f65-b444-8e2a884917bf_Saddle%20Brown.png",
    "Wall/Lap Siding/Sand Dune": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114701_d17ca0c3-172b-44ff-a010-57af84ae49f0_ba5848f2-fef8-44e7-8674-477a1bab48a7_Sand%20Dune.png",
    "Wall/Lap Siding/Sea Moss": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114832_7325267c-835e-44b3-931c-f7f3836f0a93_a40c1ed8-d3b4-47c4-9372-5fc047438d7b_Sea%20Moss.png",
    "Wall/Lap Siding/Smoke Grey": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115020_f5b1d65d-8188-4f93-aed5-755538ff6da9_906744c1-941e-4f98-bae4-8ad1692de5e2_Smoke%20Grey.png",
    "Wall/Lap Siding/Artic Blue": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-145004_28f98ca8-d1d0-4dd0-9c4c-81b01d293355_ff3e6803-c902-46e0-a877-529fb4189903_Arcatic%20Blue.png",
    # "Wall/Lap Siding/Brickstone Red": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113039_d31aa2a6-1829-4e39-a4cf-6b859c3aeed3_89c0bdd2-e1f7-45d9-95fe-c0483ffc5a4a_Brickstone%20Red.png",
    "Wall/Lap Siding/Brickstone Red": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251021-075751_6a082b94-ccf7-4860-90a5-a0992f582449_799a93b8-95c2-46e0-9d94-6cfd96b7482e_Brickstone%20Red.png",
    "Wall/Lap Siding/Cashmere": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113147_59829bdf-5f12-48c2-8580-f2b1328e83a5_1052942c-b9dd-4095-9f36-20b99532e079_Cashmere.png",
    "Wall/Lap Siding/Forest": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113420_079af740-e529-4c97-871d-886428cd997d_27329ebc-9f9a-4134-a844-eae7f2a0e283_Forest.png",
    "Wall/Lap Siding/Sage": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114447_0a04d2c1-0b65-42da-846e-92ab22124f74_7349b156-523c-4600-8691-7089d12cdaab_Sage.png",

    "Wall/Board and Batten/Artic Blue" : "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-144412_6e1bb9fc-b940-405b-8c8d-8f0420d345fa_d86ba229-e925-40ac-aedf-0ee5655c37c5_Arcatic%20Blue.png",
    "Wall/Board and Batten/Bourbon" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115415_786bd378-4ac7-4e08-9774-9491e9aeb01b_343030f8-7de9-4a21-8a2d-fcab18a06150_Bourbon.png",
    # "Wall/Board and Batten/Brickstone Red" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115525_0e84ab78-ee83-4a16-b68f-2d7f30b33715_98fbc264-5dc6-4f8b-aa4a-6a3894ddd4de_Brickstone%20Red.png",
    "Wall/Board and Batten/Brickstone Red":"https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251021-075409_a63e1f97-be90-4f42-badd-a5b3a0aeb366_4b288685-966c-44f7-b3e9-7f909bd7a9fe_Brickstone%20Red.png",
    "Wall/Board and Batten/Cashmere" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115653_c74a30d1-e94e-429f-a788-a6ad34569df0_1e0a3be3-6534-436f-85fa-8f8ab50bf267_Cashmere.png",
    "Wall/Board and Batten/Charcoal" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115817_5144b609-9ed0-48be-a7b2-03f0e48c008b_fc36dc99-f1a4-4b8c-92ec-feb8cf9c2359_Charcoal.png",
    "Wall/Board and Batten/Forest" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115929_956cfd5b-2a2f-4a95-8530-9d8c8a4ad112_b5961599-a309-41a3-9f4b-62f4adbeb3bf_Forest.png",
    "Wall/Board and Batten/Khaki" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120049_41cd85e3-c03f-4e0c-93c1-83e27fde00f6_882598f1-d56a-4134-80a0-af6f83d4d757_Khaki.png",
    "Wall/Board and Batten/Midnight" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120219_13555ac8-2780-4af4-b302-7957edc8ad26_308ecd58-97fa-404a-b2b3-5d3e52779d51_Midnight.png",
    "Wall/Board and Batten/Ocean Mist" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120348_f11d5fee-37cb-4cd6-8cf0-cddd451053a9_0e61232a-89f7-49f8-b724-4d28ee5cff95_Ocean%20Mist.png",
    "Wall/Board and Batten/Polar White" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120523_d64c4fa3-d0e8-4f08-baa0-0b82a61941e3_e66f4958-2b36-48eb-a4c1-6ba82fe5830f_Polar%20White.png",
    "Wall/Board and Batten/Saddle Brown" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120637_cef58c33-0054-404c-a229-630f9816017e_14d5d4c4-da56-4c8d-8150-43a5f0fb1e00_Saddle%20Brown.png",
    "Wall/Board and Batten/Sage" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120849_fd8dae0c-5a71-4b82-a70f-5c0021d82191_60a05285-5b70-49a9-a038-be059b8d4815_Sage.png",
    "Wall/Board and Batten/Sand Dune" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-121150_837575b0-528e-49f6-867f-b40cdb87e73c_2a286b5f-ed26-4130-a658-0884fb5f3737_Sand%20Dune.png",
    "Wall/Board and Batten/Sea Moss" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-121358_d3b23884-3aab-4322-82c0-f8ee786389cf_15266bbf-beda-4eb8-b3ef-bc7ecf9b5be4_Sea%20Moss.png",
    "Wall/Board and Batten/Smoke Grey" : "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-121710_c3ee9a35-d27e-44ee-97d4-0d497a5aff38_267140a7-2e79-40d3-b94c-d44552e2eaa5_Smoke%20Grey.png",







    #
    # # === Wall → Brick (leaf items, mapped by order) ===
    # "Wall/categories/Brick/Red":                   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch0-400.jpg",
    # "Wall/categories/Brick/Sand":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch1-400.jpg",
    # "Wall/categories/Brick/Deep Red Handmould":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch2-400.jpg",
    # "Wall/categories/Brick/Sand Rumbled":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch3-400.jpg",
    # "Wall/categories/Brick/Cream Rockface":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch4-400.jpg",
    # "Wall/categories/Brick/Dutch Molde":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch5-400.jpg",
    # "Wall/categories/Brick/Charcoal":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch6-400.jpg",
    # "Wall/categories/Brick/Cerise 1/3 Bond":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch7-400.jpg",
    # "Wall/categories/Brick/Durham Rumbled":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch8-400.jpg",
    # "Wall/categories/Brick/Silver":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch9-400.jpg",
    # "Wall/categories/Brick/Firerock King 1/3":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch10-400.jpg",
    # "Wall/categories/Brick/Mute Red":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch11-400.jpg",
    # "Wall/categories/Brick/Crimson":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch12-400.jpg",
    #
    # # === Wall → Siding (sub-category logos) ===
    # "Wall/categories/Siding/Align":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    # "Wall/categories/Siding/Aluminum":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    # "Wall/categories/Siding/Steel":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    # "Wall/categories/Siding/Vinyl":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    # "Wall/categories/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",
    #
    # # --- Siding → Align (leaf items, by order) ---
    # 'Wall/categories/Siding/Align/Align 7" Plank':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Align/Align 12" Board and Batten Matte':       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Align/Align 12" Board and Batten Woodgrain':   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",
    #
    # # --- Siding → Aluminum (9 items, by order) ---
    # "Wall/categories/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding':  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Aluminum/Longboard 4" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Aluminum/Longboard 6" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",
    #
    # # --- Siding → Steel (7 items, by order) ---
    # "Wall/categories/Siding/Steel/Distinction Siding":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Steel/Sierra Steel 8" Clapboard':                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Steel/Sierra Steel D4 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Steel/Sierra Steel D5 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Steel/Steel Side D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Steel/Steel Side D5 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",
    #
    # # --- Siding → Vinyl (23 items, by order) ---
    # "Wall/categories/Siding/Vinyl/Board and Batten":                           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Concord D4 Clapboard":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Concord D4 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Concord D5 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Driftwood II D4.5 Dutch Lap":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Driftwood II D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Fairhaven Sound Single Select Scallops":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Fairhaven Sound Single Select Shakes":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Fairweather Vertical":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Foundry FPX":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Perfection Shingle":                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Rounds":                                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Split Shake":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Vinyl/Staggered Shake 10"':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    # 'Wall/categories/Siding/Vinyl/Staggered Shake 7"':                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Oxford Premium":                              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Sequoia Select D4 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Sequoia Select D5 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Single Select Scallops":                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Vinyl/Single Select Shakes":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",
    #
    # # --- Siding → Specialty Siding (2 items, by order) ---
    # "Wall/categories/Siding/Specialty Siding/ChamClad":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    # "Wall/categories/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",
    #
    # # === Wall → Stone (brand logos) ===
    # "Wall/categories/Stone/Foundry":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2Flogo.png",
    # "Wall/categories/Stone/Gentek Canada": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2Flogo.png",
    #
    # # --- Stone → Foundry (4 items, by order) ---
    # "Wall/categories/Stone/Foundry/Cottonwood":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Foundry/Desert Canyon":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch1-400.jpg",
    # "Wall/categories/Stone/Foundry/Mesa":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch2-400.jpg",
    # "Wall/categories/Stone/Foundry/Red Rock":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch3-400.jpg",
    #
    # # --- Stone → Gentek Canada (series-level images; colors below will stay null unless provided) ---
    # "Wall/categories/Stone/Gentek Canada/Carved Block": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Ledgestone":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_Ledgestone%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut/Mission Point":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut/Plum Creek":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch1-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut/Sterling":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch2-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut/Terra Rosa":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch3-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut/Sand":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch4-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Tight Cut/Northern Ash":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch5-400.jpg",
    #
    # "Wall/categories/Stone/Gentek Canada/Ledgestone/Mission Point":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Ledgestone/Plum Creek":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch1-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Ledgestone/Sterling":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch2-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Ledgestone/Terra Rosa":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch3-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Ledgestone/Sand":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch4-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Ledgestone/Northern Ash":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch5-400.jpg",
    #
    # "Wall/categories/Stone/Gentek Canada/Carved Block/Midnight":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    # "Wall/categories/Stone/Gentek Canada/Carved Block/Sea Salt":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch1-400.jpg",
    #

    # === Accent → Categories (you already tested these) ===
    # "Accent/categories/Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2Flogo.png",
    # "Accent/categories/Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    # "Accent/categories/Stone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2Flogo.png",
    #
    # # === Accent → Brick (leaf items, mapped by order) ===
    # "Accent/categories/Brick/Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch0-400.jpg",
    # "Accent/categories/Brick/Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch1-400.jpg",
    # "Accent/categories/Brick/Deep Red Handmould": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch2-400.jpg",
    # "Accent/categories/Brick/Sand Rumbled": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch3-400.jpg",
    # "Accent/categories/Brick/Cream Rockface": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch4-400.jpg",
    # "Accent/categories/Brick/Dutch Molde": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch5-400.jpg",
    # "Accent/categories/Brick/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch6-400.jpg",
    # "Accent/categories/Brick/Cerise 1/3 Bond": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch7-400.jpg",
    # "Accent/categories/Brick/Durham Rumbled": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch8-400.jpg",
    # "Accent/categories/Brick/Silver": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch9-400.jpg",
    # "Accent/categories/Brick/Firerock King 1/3": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch10-400.jpg",
    # "Accent/categories/Brick/Mute Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch11-400.jpg",
    # "Accent/categories/Brick/Crimson": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch12-400.jpg",
    #
    # # === Accent → Siding (sub-category logos) ===
    # "Accent/categories/Siding/Align": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    # "Accent/categories/Siding/Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    # "Accent/categories/Siding/Steel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    # "Accent/categories/Siding/Vinyl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    # "Accent/categories/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",
    #
    # # --- Accent → Align (leaf items, by order) ---
    # 'Accent/categories/Siding/Align/Align 7" Plank': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Align/Align 12" Board and Batten Matte': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Align/Align 12" Board and Batten Woodgrain': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",
    #
    # # --- Accent → Aluminum (9 items, by order) ---
    # "Accent/categories/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Aluminum/Longboard 4" V Groove': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Aluminum/Longboard 6" V Groove': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",
    #
    # # --- Accent → Steel (7 items, by order) ---
    # "Accent/categories/Siding/Steel/Distinction Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Steel/Sierra Steel 8" Clapboard': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Steel/Sierra Steel D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Steel/Sierra Steel D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Steel/Steel Side D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Steel/Steel Side D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",
    #
    # # --- Accent → Vinyl (23 items, by order) ---
    # "Accent/categories/Siding/Vinyl/Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Concord D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Concord D4 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Concord D5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Driftwood II D4.5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Driftwood II D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Fairhaven Sound Single Select Scallops": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Fairhaven Sound Single Select Shakes": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Fairweather Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Foundry FPX": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Perfection Shingle": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Rounds": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Split Shake": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Vinyl/Staggered Shake 10"': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    # 'Accent/categories/Siding/Vinyl/Staggered Shake 7"': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Oxford Premium": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Sequoia Select D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Sequoia Select D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Single Select Scallops": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Vinyl/Single Select Shakes": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",
    #
    # # --- Accent → Specialty Siding (2 items, by order) ---
    # "Accent/categories/Siding/Specialty Siding/ChamClad": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    # "Accent/categories/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",
    #
    # # === Accent → Stone (brand logos) ===
    # "Accent/categories/Stone/Foundry": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2Flogo.png",
    # "Accent/categories/Stone/Gentek Canada": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2Flogo.png",
    #
    # # --- Accent → Foundry (4 items, by order) ---
    # "Accent/categories/Stone/Foundry/Cottonwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch0-400.jpg",
    # "Accent/categories/Stone/Foundry/Desert Canyon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch1-400.jpg",
    # "Accent/categories/Stone/Foundry/Mesa": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch2-400.jpg",
    # "Accent/categories/Stone/Foundry/Red Rock": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch3-400.jpg",
    #
    # # --- Accent → Gentek Canada (series-level images; colors below will stay null unless provided) ---
    # "Accent/categories/Stone/Gentek Canada/Carved Block": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Ledgestone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_Ledgestone%2F~swatch0-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Tight Cut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    #
    # "Accent/categories/Stone/Gentek Canada/Tight Cut/Mission Point": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Tight Cut/Plum Creek": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch1-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Tight Cut/Sterling": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch2-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Tight Cut/Terra Rosa": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch3-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Tight Cut/Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch4-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Tight Cut/Northern Ash": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch5-400.jpg",
    #
    # "Accent/categories/Stone/Gentek Canada/Ledgestone/Mission Point": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Ledgestone/Plum Creek": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch1-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Ledgestone/Sterling": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch2-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Ledgestone/Terra Rosa": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch3-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Ledgestone/Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch4-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Ledgestone/Northern Ash": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch5-400.jpg",
    #
    # "Accent/categories/Stone/Gentek Canada/Carved Block/Midnight": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    # "Accent/categories/Stone/Gentek Canada/Carved Block/Sea Salt": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch1-400.jpg",

    "Accent": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    "Accent/Board and Batten": "https://res.cloudinary.com/x-nabeel-x/image/upload/v1758714944/users/a203d682-0b66-4b4a-949a-59fe6209cee9/562f7e31-0f70-46cc-847a-168a430ab96f_image_1_usvhtp.png",
    "Accent/Lap Siding": "https://res.cloudinary.com/x-nabeel-x/image/upload/v1758715074/users/a203d682-0b66-4b4a-949a-59fe6209cee9/6d59f056-d8ad-4c54-9982-df6a1d66d643_image_cs2rvi.png",

    "Accent/Lap Siding/Bourbon": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-112918_3c19677c-e3b6-4caa-b883-3aedb8be9760_bcb2483e-ba34-4ab8-bba4-e0ee00f9e7b2_Bourbon.png",
    "Accent/Lap Siding/Charcoal": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113302_e2198a68-4872-4ccc-8199-8fcce0e4ea92_1417c153-2f02-42b6-8012-83baf89d6e94_Charcoal.png",
    "Accent/Lap Siding/Khaki": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113548_d9f43607-dedf-4c5c-81c9-498b6c02d70d_d29a0b8b-4d62-48dd-8560-d08e29ddcf5e_Khaki.png",
    "Accent/Lap Siding/Midnight": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113728_4b3c51bc-358b-46dd-ba26-57bf25a4bc55_e93004fc-2417-49c6-99cf-8332ed4c179f_Midnight.png",
    "Accent/Lap Siding/Ocean Mist": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113917_fc518223-7680-4871-8eac-f7f8e48b3a21_44b395a0-894f-4681-9a3d-26eeea90d888_Ocean%20Mist.png",
    "Accent/Lap Siding/Polar White": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114106_71776c25-5c9a-401d-bff1-6d66adaebb59_97eff863-3dfa-4608-a347-d241580dcde8_Polar%20White.png",
    "Accent/Lap Siding/Saddle Brown": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114237_e65b535e-32a1-4735-bfe0-476366fab176_f488f99d-25d5-4f65-b444-8e2a884917bf_Saddle%20Brown.png",
    "Accent/Lap Siding/Sand Dune": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114701_d17ca0c3-172b-44ff-a010-57af84ae49f0_ba5848f2-fef8-44e7-8674-477a1bab48a7_Sand%20Dune.png",
    "Accent/Lap Siding/Sea Moss": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114832_7325267c-835e-44b3-931c-f7f3836f0a93_a40c1ed8-d3b4-47c4-9372-5fc047438d7b_Sea%20Moss.png",
    "Accent/Lap Siding/Smoke Grey": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115020_f5b1d65d-8188-4f93-aed5-755538ff6da9_906744c1-941e-4f98-bae4-8ad1692de5e2_Smoke%20Grey.png",
    "Accent/Lap Siding/Artic Blue": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-145004_28f98ca8-d1d0-4dd0-9c4c-81b01d293355_ff3e6803-c902-46e0-a877-529fb4189903_Arcatic%20Blue.png",
    # "Accent/Lap Siding/Brickstone Red": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113039_d31aa2a6-1829-4e39-a4cf-6b859c3aeed3_89c0bdd2-e1f7-45d9-95fe-c0483ffc5a4a_Brickstone%20Red.png",
    "Accent/Lap Siding/Brickstone Red": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251021-075751_6a082b94-ccf7-4860-90a5-a0992f582449_799a93b8-95c2-46e0-9d94-6cfd96b7482e_Brickstone%20Red.png",
    "Accent/Lap Siding/Cashmere": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113147_59829bdf-5f12-48c2-8580-f2b1328e83a5_1052942c-b9dd-4095-9f36-20b99532e079_Cashmere.png",
    "Accent/Lap Siding/Forest": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-113420_079af740-e529-4c97-871d-886428cd997d_27329ebc-9f9a-4134-a844-eae7f2a0e283_Forest.png",
    "Accent/Lap Siding/Sage": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-114447_0a04d2c1-0b65-42da-846e-92ab22124f74_7349b156-523c-4600-8691-7089d12cdaab_Sage.png",

    "Accent/Board and Batten/Artic Blue": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-144412_6e1bb9fc-b940-405b-8c8d-8f0420d345fa_d86ba229-e925-40ac-aedf-0ee5655c37c5_Arcatic%20Blue.png",
    "Accent/Board and Batten/Bourbon": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115415_786bd378-4ac7-4e08-9774-9491e9aeb01b_343030f8-7de9-4a21-8a2d-fcab18a06150_Bourbon.png",
    # "Accent/Board and Batten/Brickstone Red": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115525_0e84ab78-ee83-4a16-b68f-2d7f30b33715_98fbc264-5dc6-4f8b-aa4a-6a3894ddd4de_Brickstone%20Red.png",
    "Accent/Board and Batten/Brickstone Red":"https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251021-075409_a63e1f97-be90-4f42-badd-a5b3a0aeb366_4b288685-966c-44f7-b3e9-7f909bd7a9fe_Brickstone%20Red.png",
    "Accent/Board and Batten/Cashmere": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115653_c74a30d1-e94e-429f-a788-a6ad34569df0_1e0a3be3-6534-436f-85fa-8f8ab50bf267_Cashmere.png",
    "Accent/Board and Batten/Charcoal": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115817_5144b609-9ed0-48be-a7b2-03f0e48c008b_fc36dc99-f1a4-4b8c-92ec-feb8cf9c2359_Charcoal.png",
    "Accent/Board and Batten/Forest": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-115929_956cfd5b-2a2f-4a95-8530-9d8c8a4ad112_b5961599-a309-41a3-9f4b-62f4adbeb3bf_Forest.png",
    "Accent/Board and Batten/Khaki": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120049_41cd85e3-c03f-4e0c-93c1-83e27fde00f6_882598f1-d56a-4134-80a0-af6f83d4d757_Khaki.png",
    "Accent/Board and Batten/Midnight": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120219_13555ac8-2780-4af4-b302-7957edc8ad26_308ecd58-97fa-404a-b2b3-5d3e52779d51_Midnight.png",
    "Accent/Board and Batten/Ocean Mist": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120348_f11d5fee-37cb-4cd6-8cf0-cddd451053a9_0e61232a-89f7-49f8-b724-4d28ee5cff95_Ocean%20Mist.png",
    "Accent/Board and Batten/Polar White": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120523_d64c4fa3-d0e8-4f08-baa0-0b82a61941e3_e66f4958-2b36-48eb-a4c1-6ba82fe5830f_Polar%20White.png",
    "Accent/Board and Batten/Saddle Brown": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120637_cef58c33-0054-404c-a229-630f9816017e_14d5d4c4-da56-4c8d-8150-43a5f0fb1e00_Saddle%20Brown.png",
    "Accent/Board and Batten/Sage": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-120849_fd8dae0c-5a71-4b82-a70f-5c0021d82191_60a05285-5b70-49a9-a038-be059b8d4815_Sage.png",
    "Accent/Board and Batten/Sand Dune": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-121150_837575b0-528e-49f6-867f-b40cdb87e73c_2a286b5f-ed26-4130-a658-0884fb5f3737_Sand%20Dune.png",
    "Accent/Board and Batten/Sea Moss": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-121358_d3b23884-3aab-4322-82c0-f8ee786389cf_15266bbf-beda-4eb8-b3ef-bc7ecf9b5be4_Sea%20Moss.png",
    "Accent/Board and Batten/Smoke Grey": "https://insta-sammy-home-visualiser.s3.us-west-2.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251020-121710_c3ee9a35-d27e-44ee-97d4-0d497a5aff38_267140a7-2e79-40d3-b94c-d44552e2eaa5_Smoke%20Grey.png",

    # === Masonry → Categories (you already tested these) ===
    # "Masonry/categories/Brick":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2Flogo.png",
    # "Masonry/categories/Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    # "Masonry/categories/Stone":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2Flogo.png",

    # # === Masonry → Brick (leaf items, mapped by order) ===
    # "Masonry/categories/Brick/Red":                   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch0-400.jpg",
    # "Masonry/categories/Brick/Sand":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch1-400.jpg",
    # "Masonry/categories/Brick/Deep Red Handmould":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch2-400.jpg",
    # "Masonry/categories/Brick/Sand Rumbled":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch3-400.jpg",
    # "Masonry/categories/Brick/Cream Rockface":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch4-400.jpg",
    # "Masonry/categories/Brick/Dutch Molde":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch5-400.jpg",
    # "Masonry/categories/Brick/Charcoal":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch6-400.jpg",
    # "Masonry/categories/Brick/Cerise 1/3 Bond":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch7-400.jpg",
    # "Masonry/categories/Brick/Durham Rumbled":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch8-400.jpg",
    # "Masonry/categories/Brick/Silver":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch9-400.jpg",
    # "Masonry/categories/Brick/Firerock King 1/3":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch10-400.jpg",
    # "Masonry/categories/Brick/Mute Red":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch11-400.jpg",
    # "Masonry/categories/Brick/Crimson":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch12-400.jpg",
    #
    # # === Masonry → Siding (sub-category logos) ===
    # "Masonry/categories/Siding/Align":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    # "Masonry/categories/Siding/Aluminum":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    # "Masonry/categories/Siding/Steel":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    # "Masonry/categories/Siding/Vinyl":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    # "Masonry/categories/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",
    #
    # # --- Siding → Align (leaf items, by order) ---
    # 'Masonry/categories/Siding/Align/Align 7" Plank':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Align/Align 12" Board and Batten Matte':       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Align/Align 12" Board and Batten Woodgrain':   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",
    #
    # # --- Siding → Aluminum (9 items, by order) ---
    # "Masonry/categories/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding':  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Aluminum/Longboard 4" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Aluminum/Longboard 6" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",
    #
    # # --- Siding → Steel (7 items, by order) ---
    # "Masonry/categories/Siding/Steel/Distinction Siding":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Steel/Sierra Steel 8" Clapboard':                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Steel/Sierra Steel D4 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Steel/Sierra Steel D5 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Steel/Steel Side D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Steel/Steel Side D5 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",
    #
    # # --- Siding → Vinyl (23 items, by order) ---
    # "Masonry/categories/Siding/Vinyl/Board and Batten":                           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Concord D4 Clapboard":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Concord D4 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Concord D5 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Driftwood II D4.5 Dutch Lap":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Driftwood II D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Fairhaven Sound Single Select Scallops":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Fairhaven Sound Single Select Shakes":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Fairweather Vertical":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Foundry FPX":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Perfection Shingle":                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Rounds":                                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Split Shake":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Vinyl/Staggered Shake 10"':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    # 'Masonry/categories/Siding/Vinyl/Staggered Shake 7"':                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Oxford Premium":                              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Sequoia Select D4 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Sequoia Select D5 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Single Select Scallops":                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Vinyl/Single Select Shakes":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",
    #
    # # --- Siding → Specialty Siding (2 items, by order) ---
    # "Masonry/categories/Siding/Specialty Siding/ChamClad":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    # "Masonry/categories/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",
    #
    # # === Wall → Stone (brand logos) ===
    # "Masonry/categories/Stone/Foundry":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2Flogo.png",
    # "Masonry/categories/Stone/Gentek Canada": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2Flogo.png",
    #
    # # --- Stone → Foundry (4 items, by order) ---
    # "Masonry/categories/Stone/Foundry/Cottonwood":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Foundry/Desert Canyon":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch1-400.jpg",
    # "Masonry/categories/Stone/Foundry/Mesa":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch2-400.jpg",
    # "Masonry/categories/Stone/Foundry/Red Rock":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch3-400.jpg",
    #
    # # --- Stone → Gentek Canada (series-level images; colors below will stay null unless provided) ---
    # "Masonry/categories/Stone/Gentek Canada/Carved Block": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_Ledgestone%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut/Mission Point": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut/Plum Creek": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch1-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut/Sterling": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch2-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut/Terra Rosa": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch3-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut/Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch4-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Tight Cut/Northern Ash": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch5-400.jpg",
    #
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone/Mission Point": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone/Plum Creek": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch1-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone/Sterling": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch2-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone/Terra Rosa": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch3-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone/Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch4-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Ledgestone/Northern Ash": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch5-400.jpg",
    #
    # "Masonry/categories/Stone/Gentek Canada/Carved Block/Midnight": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    # "Masonry/categories/Stone/Gentek Canada/Carved Block/Sea Salt": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch1-400.jpg",

    # Aluminum Trim & Accessories (logo)
    # "Trim/categories/Aluminum Trim and Accessories": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png",
    # "Trim/categories/Vinyl Trim and Accessories": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png",
    # "Trim/categories/Gentek Performance G8 Piece": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png",


    # Aluminum Trim & Accessories
    "Trim/Metallic Gray":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch12-400.jpg",
    "Trim/Sable":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Trim/Wedgewood Blue":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Trim/Ivy Green":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Trim/Chestnut Brown":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Trim/Nutmeg":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Trim/Antique Brown":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Trim/Forest Green":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Trim/Graphite":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch32-400.jpg",
    # Vinyl Trim & Accessories
    "Trim/Canyon Clay":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch2-400.jpg",
    "Trim/Chesapeake Gray":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch3-400.jpg",
    "Trim/Coastal Blue":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch4-400.jpg",
    "Trim/Dark Drift":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch5-400.jpg",
    "Trim/Espresso":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch7-400.jpg",
    "Trim/Hudson Slate":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch8-400.jpg",
    "Trim/Juniper Grove":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch10-400.jpg",
    "Trim/Majestic Brick":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch13-400.jpg",
    "Trim/Marine Dusk":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch14-400.jpg",
    "Trim/Meadow Fern":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch15-400.jpg",
    "Trim/Midnight Surf":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Trim/Moonlit Moss":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch18-400.jpg",
    "Trim/Pearl":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Trim/Rockport Brown":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch21-400.jpg",
    "Trim/Rockwell Blue":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Trim/Sage":                   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch23-400.jpg",
    "Trim/Smoked Timber":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch25-400.jpg",
    "Trim/Storm":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Trim/Wicker":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch28-400.jpg",
    "Trim/Windswept Smoke":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Trim/BarnBoard Grey":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Trim/Honey Super Matte":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Trim/Super Matte Modern Walnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Trim/Sun Bleached Oak":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch33-400.jpg",
    "Trim/Cinnamon Walnut":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch34-400.jpg",
    "Trim/Barrel Oak":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Trim/Toffee":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Trim/Charred Black":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Trim/Atlantic White":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Trim/Chai Cedar":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Trim/Brushed Metallic":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch40-400.jpg",

    # Gentek Performance G8 Piece
    "Trim/Pebble":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch2-400.jpg",
    "Trim/Commercial Brown":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch3-400.jpg",
    "Trim/Slate":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch4-400.jpg",
    "Trim/Iron Ore":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch5-400.jpg",
    "Trim/Black":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch6-400.jpg",

    # "Window and Door Trim/categories/Aluminum Trim and Accessories": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png",
    # "Window and Door Trim/categories/Vinyl Trim and Accessories": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png",
    # "Window and Door Trim/categories/Gentek Performance G8 Piece": "https://sammy-home-visualiser.s3.eu-north-1.amazonaws.com/users/73c57bbd-3437-4cf0-bc35-66a04ec850c9/20251001-074914_ac181a2f-dd11-4756-aeeb-7ae24de2d24a_50896c6f-6290-4d07-94a9-aeed227ec760_logo.png",


    # Aluminum Trim & Accessories (logo)
    "Window and Door Trim/Metallic Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch12-400.jpg",
    "Window and Door Trim/Sage": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch13-400.jpg",
    "Window and Door Trim/Juniper Grove": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch14-400.jpg",
    "Window and Door Trim/Storm": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch15-400.jpg",
    "Window and Door Trim/Sable": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Window and Door Trim/Windswept Smoke": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch17-400.jpg",
    "Window and Door Trim/Midnight Surf": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch18-400.jpg",
    "Window and Door Trim/Wedgewood Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Window and Door Trim/Rockwell Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch20-400.jpg",
    "Window and Door Trim/Coastal Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch21-400.jpg",
    "Window and Door Trim/Ivy Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Window and Door Trim/Dark Drift": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch24-400.jpg",
    "Window and Door Trim/Espresso": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch25-400.jpg",
    "Window and Door Trim/Moonlit Moss": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch26-400.jpg",
    "Window and Door Trim/Chestnut Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Window and Door Trim/Nutmeg": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Window and Door Trim/Antique Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Window and Door Trim/Forest Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Window and Door Trim/Graphite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Window and Door Trim/Chesapeake Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Window and Door Trim/Majestic Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Window and Door Trim/Rockport Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Window and Door Trim/Smoked Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Window and Door Trim/Meadow Fern": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Window and Door Trim/Marine Dusk": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch40-400.jpg",
    "Window and Door Trim/Hudson Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch41-400.jpg",

    # Vinyl Trim & Accessories
    "Window and Door Trim/Canyon Clay": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch2-400.jpg",
    "Window and Door Trim/Iron Ore": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch9-400.jpg",
    "Window and Door Trim/Pearl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Window and Door Trim/Pebble": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch20-400.jpg",
    "Window and Door Trim/Wicker": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch28-400.jpg",
    "Window and Door Trim/BarnBoard Grey": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Window and Door Trim/Honey Super Matte": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Window and Door Trim/Super Matte Modern Walnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Window and Door Trim/Sun Bleached Oak": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch33-400.jpg",
    "Window and Door Trim/Cinnamon Walnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch34-400.jpg",
    "Window and Door Trim/Barrel Oak": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Window and Door Trim/Toffee": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Window and Door Trim/Charred Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Window and Door Trim/Atlantic White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Window and Door Trim/Chai Cedar": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Window and Door Trim/Brushed Metallic": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch40-400.jpg",

    # Gentek Performance G8 Piece
    "Window and Door Trim/Commercial Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch3-400.jpg",
    "Window and Door Trim/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch4-400.jpg",
    "Window and Door Trim/Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch6-400.jpg",

    # # -------------------- ROOFING / GAF --------------------
    #
    # # 3-Tab (group + series logos)
    # "Roof/categories/3-Tab": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2Flogo.png",
    # "Roof/categories/3-Tab/Marquis Weathermax": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2Flogo.png",
    # "Roof/categories/3-Tab/Royal Sovereign": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2Flogo.png",
    #
    # # 3-Tab / Marquis Weathermax® (swatches)
    # "Roof/categories/3-Tab/Marquis Weathermax/Autumn Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2F~swatch0-400.jpg",
    # "Roof/categories/3-Tab/Marquis Weathermax/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2F~swatch1-400.jpg",
    # "Roof/categories/3-Tab/Marquis Weathermax/Weathered Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2F~swatch2-400.jpg",
    #
    # # 3-Tab / Royal Sovereign® (swatches)
    # "Roof/categories/3-Tab/Royal Sovereign/Ash Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch0-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Silver Lining": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch1-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch2-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Summer Sage": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch3-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch4-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Weathered Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch5-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Autumn Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch6-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch7-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Cypress Tan": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch8-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Golden Cedar": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch9-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Nickel Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch10-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Russet Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch11-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Sandrift": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch12-400.jpg",
    # "Roof/categories/3-Tab/Royal Sovereign/Desert Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch13-400.jpg",
    #
    # # Designer (series logos)
    # "Roof/categories/Designer": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2Flogo.png",
    # "Roof/categories/Designer/Camelot II": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2Flogo.png",
    # "Roof/categories/Designer/Glenwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2Flogo.png",
    # "Roof/categories/Designer/Grand Canyon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2Flogo.png",
    # "Roof/categories/Designer/Grand Sequoia": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2Flogo.png",
    # "Roof/categories/Designer/Grand Sequoia AS": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2Flogo.png",
    # "Roof/categories/Designer/Grand Sequoia RS": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2Flogo.png",
    # "Roof/categories/Designer/Grand Sequoia RS+": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRSPlus%2Flogo.png",
    # "Roof/categories/Designer/Slateline": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2Flogo.png",
    # "Roof/categories/Designer/Woodland": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2Flogo.png",
    #
    # # Designer / Camelot II (swatches)
    # "Roof/categories/Designer/Camelot II/Barkwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Camelot II/Weathered Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Camelot II/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Camelot II/Antique Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Camelot II/Royal Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch4-400.jpg",
    # "Roof/categories/Designer/Camelot II/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch5-400.jpg",
    #
    # # Designer / Glenwood® (swatches)
    # "Roof/categories/Designer/Glenwood/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Glenwood/Golden Prairie": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Glenwood/Autumn Harvest": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Glenwood/Dusky Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Glenwood/Adobe Clay": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch4-400.jpg",
    # "Roof/categories/Designer/Glenwood/Chelsea Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch5-400.jpg",
    #
    # # Designer / Grand Canyon™ (swatches)
    # "Roof/categories/Designer/Grand Canyon/Stonewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Grand Canyon/Black Oak": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Grand Canyon/Mission Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Grand Canyon/Storm Cloud": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Grand Canyon/Sedona Sunset": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch4-400.jpg",
    #
    # # Designer / Grand Sequoia® (swatches)
    # "Roof/categories/Designer/Grand Sequoia/Autumn Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia/Cedar": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia/Mesa Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch4-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia/Weathered Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch5-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch6-400.jpg",
    #
    # # Designer / Grand Sequoia® AS (swatches)
    # "Roof/categories/Designer/Grand Sequoia AS/Adobe Sunset": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia AS/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia AS/Dusky Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia AS/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch3-400.jpg",
    #
    # # Designer / Grand Sequoia® RS (swatches)
    # "Roof/categories/Designer/Grand Sequoia RS/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia RS/Forest Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia RS/Ocean Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia RS/Sagewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia RS/Sandalwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch4-400.jpg",
    #
    # # Designer / Grand Sequoia® RS+ (swatches)
    # "Roof/categories/Designer/Grand Sequoia RS+/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRSPlus%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Grand Sequoia RS+/Forest Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRSPlus%2F~swatch1-400.jpg",
    #
    # # Designer / Slateline® (swatches)
    # "Roof/categories/Designer/Slateline/Antique Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Slateline/Emerald Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Slateline/English Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Slateline/Royal Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Slateline/Weathered Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch4-400.jpg",
    #
    # # Designer / Woodland (swatches)
    # "Roof/categories/Designer/Woodland/Castlewood Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch0-400.jpg",
    # "Roof/categories/Designer/Woodland/Cedarwood Abbey": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch1-400.jpg",
    # "Roof/categories/Designer/Woodland/Tuscan Sunset": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch2-400.jpg",
    # "Roof/categories/Designer/Woodland/Woodberry Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch3-400.jpg",
    # "Roof/categories/Designer/Woodland/Canterbury Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch4-400.jpg",
    #
    # "Roof/categories/Timberline Roofing Shingles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline CS" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineCS%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2Flogo.png",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD" : "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2Flogo.png",
    #
    #
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Amber Wheat":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Appalachian Sky":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Golden Harvest":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Cedar Falls":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Midnight Blush":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Adobe Sunset":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Brandywine Dusk":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch6-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Nantucket Morning":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch7-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AH/Saddlewood Ranch":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineAH%2F~swatch8-400.jpg",
    #
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Charcoal":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Barkwood":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Hickory":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Pewter Gray":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Shakewood":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Slate":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline AS II/Weathered Wood":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineASII%2F~swatch6-400.jpg",
    #
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline CS/Antique Slate":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineCS%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline CS/Barkwood":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineCS%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline CS/Weathered Wood":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineCS%2F~swatch2-400.jpg",
    #
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Barkwood":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Charcoal":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Hunter Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Mission Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Hickory": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Oyster Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Patriot Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch6-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Shakewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch7-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Pewter Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch8-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch9-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Sunset Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch10-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch11-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Birchwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch12-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch13-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Williamsburg Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch14-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Biscayne Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch15-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Canadian Driftwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch16-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Copper Canyon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch17-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Driftwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch18-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Golden Amber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch19-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HD/Fox Hollow Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHD%2F~swatch20-400.jpg",
    #
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Birchwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Barkwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Driftwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Hickory": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Hunter Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Mission Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch6-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Oyster Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch7-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Pewter Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch8-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Shakewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch9-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch10-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZ%2F~swatch11-400.jpg",
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Stone Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Hickory": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Copper Canyon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Aged Chestnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Coastal Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Sagewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch6-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Birchwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch7-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Sandalwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch8-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline HDZ RS/Golden Amber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineHDZRS%2F~swatch9-400.jpg",
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Barkwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch0-400.jpg	",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Arctic White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Hickory": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Pewter Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Shakewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch6-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Hunter Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch7-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline NS/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineNS%2F~swatch8-400.jpg",
    #
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Barkwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch0-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Birchwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch1-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch2-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Fox Hollow Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch3-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Hickory": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch4-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Hunter Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch5-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Pewter Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch6-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Patriot Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch7-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Shakewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch8-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch9-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch10-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Biscayne Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch11-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Oyster Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch12-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/Sunset Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch13-400.jpg",
    # "Roof/categories/Timberline Roofing Shingles/Timberline UHD/White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FTimberline%20Roofing%20Shingles%2F~TimberlineUHD%2F~swatch14-400.jpg",
    #
    #
    # "Door/categories/Steel Doors": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2Flogo.pngDoors",
    #
    # "Door/categories/Steel Doors/Configuration/L Door": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FDoor.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/R Door": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FDoor.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/S - Door": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSide_Door.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/Door - S": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FDoor_Side.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/S - L Door - S": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSide_Door_Side.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/S - R Door - S": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSide_Door_Side.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/Double Door": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FDoor_Door.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/S - Double Door - S": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSide_Door_Door_Side.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Configuration/Side": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSide.jpg.thumbnail.png",
    #
    #
    # "Door/categories/Steel Doors/Panel/Full Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FES-686-STL_Full-Lite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/3/4 Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCTA-607-STL_3_4_Lite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/684": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FGD-684-STL_1_2_Lite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/637": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-637CL-STL_Half_View.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/640": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FFS-640-STL_9-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/648": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-648-STL_4-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/659": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-659CL-STL_4-Panel_Sunburst.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/692": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-692CL-STL_Twin_Lite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/422": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-422CL-STL_Twin_Lite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/911": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FES-919-STL_Flush_Full_Oval.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/CT-22 - 2 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-22_2-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/CT-24 - 2 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-24_2-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/3 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-30-STL_3-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/8 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-80-STL_8-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/9 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-90-STL_9-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/4 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FES-40-STL_4-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/Flush": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FES-100-STL_Flush.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/6 Panel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCT-60-STL_6-Panel.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/Craftsman": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSteel-Craftsman-Door.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/814": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSteel-814.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/817": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSteel-817.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Panel/818": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FSteel-818.jpg.thumbnail.png",
    #
    #
    # "Door/categories/Steel Doors/Glass/Aragon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686AGGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Avant": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686AVGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Avalon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686ANGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Bellflower": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686BLF_GO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Beveled Elegance (Brass Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686BEBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Bristol (Brass Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686BTBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Bristol (Satin Nickel Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686BTSNGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Casablanca": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686CSB_GO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Catalina": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686CAGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Cut Crystal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686CCGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Cadence": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686CDGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Cirrus": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686CRGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Entropy": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686ENGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Expression (Brass Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686EXBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Expression (Satin Nickel Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686EXSNGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Greenfield": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686GRF_GO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Heirlooms (Brass Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686HMBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Heirlooms (Satin Nickel Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686HMSNGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Jacinto": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686JAGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Oak Park": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686KPGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Impression": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686LIGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Legacy Master (Brass Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686LMBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Legacy Master (Pewter Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686LMPGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Mediteranian": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MDGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Majestic (Brass Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MEBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Majestic (Nickel Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MENGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Majestic (Pewter Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MEPGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Madison": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MIGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Nouveau": "(Brass Caming) https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MNBGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Nouveau (Nickel Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MNNGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Monterey (Satin Nickel Caming)": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686MOSNGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Prairie Bevel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686PRGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Paris": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686PSGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Radiant Hues": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686RAGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Simplicity": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686SMGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Teton": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686TEGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Tilt and Raise Blinds": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686RBLGO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Topaz": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686TPZ_GO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Trace": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686TRC_GO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Verdana": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686VR_GO.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Clear": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686_CL_DoorLite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Clear Colonial 2x5": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686_628_CL_DoorLite.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Clear Colonial 3x5": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686_FullView.jpg.thumbnail.png",
    # "Door/categories/Steel Doors/Glass/Clear Prairie": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2F686_701_CL_DoorLite.jpg.thumbnail.png",
    #
    # "Door/categories/Steel Doors/Side" :" ",
    # "Door/categories/Steel Doors/Side Glass":"",
    #
    #
    # "Door/categories/Steel Doors/Handles/Amherst Satin Chrome": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FAmherst_Satin_Chrome_thumb.png",
    # "Door/categories/Steel Doors/Handles/Ashfield Venetian Bronze": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FAshfield_Venetian_Bronze_thumb.png",
    # "Door/categories/Steel Doors/Handles/Wellington Satin Chrome": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FWellington_Satin_Chrome_thumb.png",
    # "Door/categories/Steel Doors/Handles/Commonwealth Bright Brass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCommonwealth_Lever_BrightBrass.png.thumbnail.png",
    # "Door/categories/Steel Doors/Handles/Commonwealth Satin Nickel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCommon_Satin_Nickel_thumb.png",
    # "Door/categories/Steel Doors/Handles/Commonwealth Venetian Bronze": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FCommon_Venetian_Bronze_thumb.png",
    # "Door/categories/Steel Doors/Handles/Dorian Antique Brass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FEntry%20Doors%2F~SteelDoors%2F~grid%2FDorian_Antique_Brass_thumb.png",
    #
    #
    #
    #
    #
    #
    #
    # "Window/categories/Regency": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2Flogo.png",
    # "Window/categories/Regency 400": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2Flogo.png",
    #
    #
    #
    # "Window/categories/Regency/Regency Awning":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2Flogo.png",
    # "Window/categories/Regency/Regency Casement": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2Flogo.png",
    # "Window/categories/Regency/Regency Hung": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2Flogo.png",
    # "Window/categories/Regency/Regency Picture": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Picture%2Flogo.png",
    # "Window/categories/Regency/Regency Slider": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2Flogo.png",
    #
    #
    # "Window/categories/Regency/Regency Awning/Configuration/Single": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fawning.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Awning/Configuration/Picture over Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FFixed%20Frame%20over%20Awning.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Awning/Configuration/Double Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2F2-High_Awning.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Awning/Configuration/Awning/Picture": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2F2-Wide_Awning.jpg.thumbnail.png",
    #
    #
    # "Window/categories/Regency/Regency Awning/Exterior Finish": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FGWD_260A.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency/Regency Awning/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency/Regency Awning/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FClassic.png",
    # "Window/categories/Regency/Regency Awning/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Awning/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency/Regency Awning/Grille Type/Simulated Divided Lites 1 1/4":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Awning/Grille Type/Simulated Divided Lites 2":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Awning/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    # "Window/categories/Regency/Regency Awning/Grille Style/Colonial": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FColonial.png",
    # "Window/categories/Regency/Regency Awning/Grille Style/Diamond": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FDiamond.png",
    # "Window/categories/Regency/Regency Awning/Grille Style/Prairie": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FPrairie.png",
    # "Window/categories/Regency/Regency Awning/Grille Style/Double Prairie": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2FDouble-Prairie.png",
    #
    #
    # "Window/categories/Regency/Regency Awning/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency/Regency Awning/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency/Regency Awning/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency/Regency Awning/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency/Regency Awning/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency/Regency Awning/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    #
    # "Window/categories/Regency/Regency Casement/Configuration/Single Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-L.png",
    # "Window/categories/Regency/Regency Casement/Configuration/Single Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-R.png",
    # "Window/categories/Regency/Regency Casement/Configuration/2 Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-LO.png",
    # "Window/categories/Regency/Regency Casement/Configuration/2 Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-OR.png",
    # "Window/categories/Regency/Regency Casement/Configuration/3 Lite - L/Picture/R": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-LPR.png",
    # "Window/categories/Regency/Regency Casement/Configuration/4 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-4Lite.png",
    # "Window/categories/Regency/Regency Casement/Configuration/4 Lite - L/P/P/R": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-4Lite-LPPR.png",
    # "Window/categories/Regency/Regency Casement/Configuration/5 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-5Lite.png",
    #
    #
    # "Window/categories/Regency/Regency Casement/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FGWD_260A.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency/Regency Casement/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency/Regency Casement/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency/Regency Casement/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Casement/Grille Type/Simulated Divided Lites 1 1/4": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Casement/Grille Type/Simulated Divided Lites 2": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Casement/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency/Regency Casement/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    #
    # "Window/categories/Regency/Regency Casement/Grille Style": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2F0-NONE_thumb.jpg",
    #
    #
    # "Window/categories/Regency/Regency Casement/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency/Regency Casement/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency/Regency Casement/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency/Regency Casement/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency/Regency Casement/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency/Regency Casement/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    # "Window/categories/Regency/Regency Hung/Configuration/1 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fdouble_hung_config_W.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Hung/Configuration/2 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fdouble_hung_config_WW.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Hung/Configuration/3 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fdouble_hung_config_WWW.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Hung/Configuration/4 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fhung-4-Lite.png",
    # "Window/categories/Regency/Regency Hung/Configuration/Hung/Picture/Hung": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fhung-picture-hung.jpg",
    #
    #
    # "Window/categories/Regency/Regency Hung/Configuration/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F20Series_DH.png.thumbnail.png",
    #
    #
    #
    # "Window/categories/Regency/Regency Hung/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency/Regency Hung/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency/Regency Hung/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Hung/Grille Type/Simulated Divided Lites 1 1/4":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Hung/Grille Type/Simulated Divided Lites 2": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Hung/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency/Regency Hung/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    #
    # "Window/categories/Regency/Regency Hung/Grille Style/No Grilles Selected": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F0-NONE_thumb.jpg",
    #
    #
    # "Window/categories/Regency/Regency Hung/Glass/Light Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2FDouble_Pane.jpg",
    # "Window/categories/Regency/Regency Hung/Glass/Dark Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2FDouble_Pane.jpg",
    # "Window/categories/Regency/Regency Hung/Glass/Beveled-Leaded St. Joseph": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0003_St.-Joseph.png.thumbnail.png",
    # "Window/categories/Regency/Regency Hung/Glass/Beveled-Leaded Jackson": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0002_Jackson.png.thumbnail.png",
    # "Window/categories/Regency/Regency Hung/Glass/Beveled-Leaded Hanna": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0001_Hanna.png.thumbnail.png",
    # "Window/categories/Regency/Regency Hung/Glass/Beveled-Leaded Vicksburg": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0000_Vicksburg.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency/Regency Picture/Configuration/Single": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Picture%2F~grid%2Fawning.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Picture/Configuration/Picture over Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Picture%2F~grid%2FFixed%20Frame%20over%20Awning.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Picture/Configuration/Double Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Picture%2F~grid%2F2-High_Awning.jpg.thumbnail.png",
    # "Window/categories/Regency/Regency Picture/Configuration/Awning/Picture": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Picture%2F~grid%2F2-Wide_Awning.jpg.thumbnail.png",
    #
    # "Window/categories/Regency/Regency Picture/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Picture%2F~grid%2FGWD_260A.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency/Regency Picture/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency/Regency Picture/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency/Regency Picture/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency/Regency Picture/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categoriesRegency/Regency Picture/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categoriesRegency/Regency Picture/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    # "Window/categories/Regency/Regency Slider/Configuration/2 Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FOX.png.thumbnail.png",
    # "Window/categories/Regency/Regency Slider/Configuration/2 Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FXO.png.thumbnail.png",
    # "Window/categories/Regency/Regency Slider/Configuration/Picture over 2 Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FP-OX.png.thumbnail.png",
    # "Window/categories/Regency/Regency Slider/Configuration/Picture over 2 Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FP-XO.png.thumbnail.png",
    #
    # "Window/categories/Regency/Regency Slider/Exterior Finish/Definity Vinyl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2F20Series_DH.png.thumbnail.png",
    #
    # "Window/categories/Regency/Regency Slider/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency/Regency Slider/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency/Regency Slider/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Slider/Grille Type/Simulated Divided Lites 1 1/4": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Slider/Grille Type/Simulated Divided Lites 2" :"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency/Regency Slider/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency/Regency Slider/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    # "Window/categories/Regency/Regency Slider/Grille Style/No Grids Selected": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2F0-NONE_thumb.jpg",
    #
    # "Window/categories/Regency/Regency Slider/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency/Regency Slider/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency/Regency Slider/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency/Regency Slider/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency/Regency Slider/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency/Regency Slider/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2Flogo.png",
    # "Window/categories/Regency 400/Regency 400 Casement": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Casement%2Flogo.png",
    # "Window/categories/Regency 400/Regency 400 Hung": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Hung%2Flogo.png",
    # "Window/categories/Regency 400/Regency 400 Picture": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Picture%2Flogo.png",
    # "Window/categories/Regency 400/Regency 400 Slider": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Sliding%2Flogo.png",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Awning/Configuration/Single": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2Fawning.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Configuration/Picture over Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2FFixed%20Frame%20over%20Awning.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Configuration/Double Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2F2-High_Awning.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Configuration/Awning/Picture": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2F2-Wide_Awning.jpg.thumbnail.png",
    #
    # "Window/categories/Regency 400/Regency 400 Awning/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2FGWD_260A.png.thumbnail.png",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/": "",
    #
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/Simulated Divided Lites 1 1/4": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/Simulated Divided Lites 2" :"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Awning/Grille Style/No Grilles Selected": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2F0-NONE_thumb.jpg",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Awning/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Awning/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Awning/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency 400/Regency 400 Awning/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency 400/Regency 400 Awning/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency 400/Regency 400 Awning/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/Single Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-L.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/Single Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-R.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/2 Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-LO.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/2 Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-OR.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/3 Lite - L/Picture/R": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-LPR.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/4 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-4Lite.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/4 Lite - L/P/P/R": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-4Lite-LPPR.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Configuration/5 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FCasement-5Lite.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Casement/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Casement%2F~grid%2FGWD_260A.png.thumbnail.png",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/Simulated Divided Lites 1 1/4" :"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/Simulated Divided Lites 2" :"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Casement/Grille Style/No Grilles Selected": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Casement%2F~grid%2F0-NONE_thumb.jpg",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Casement/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Casement/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Casement/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency 400/Regency 400 Casement/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency 400/Regency 400 Casement/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency 400/Regency 400 Casement/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Hung/Configuration/1 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fdouble_hung_config_W.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Configuration/2 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fdouble_hung_config_WW.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Configuration/3 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fdouble_hung_config_WWW.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Configuration/4 Lite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fhung-4-Lite.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Configuration/Hung/Picture/Hung": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2Fhung-picture-hung.jpg",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Hung/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Hung%2F~grid%2F20Series_DH.png.thumbnail.png",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/Simulated Divided Lites 1 1/4":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/Simulated Divided Lites 2":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Hung/Grille Style/No Grilles Selected": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Hung%2F~grid%2F0-NONE_thumb.jpg",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Hung/Glass/Light Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2FDouble_Pane.jpg",
    # "Window/categories/Regency 400/Regency 400 Hung/Glass/Dark Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2FDouble_Pane.jpg",
    # "Window/categories/Regency 400/Regency 400 Hung/Glass/Beveled-Leaded St. Joseph": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0003_St.-Joseph.png.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Glass/Beveled-Leaded Jackson": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0002_Jackson.png.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Glass/Beveled-Leaded Hanna": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0001_Hanna.png.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Hung/Glass/Beveled-Leaded Vicksburg": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Hung%2F~grid%2F_0000_Vicksburg.png.thumbnail.png",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Picture/Configuration/Single": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2Fawning.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Picture/Configuration/Picture over Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2FFixed%20Frame%20over%20Awning.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Picture/Configuration/Double Awning": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2F2-High_Awning.jpg.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Picture/Configuration/Awning/Picture": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Awning%2F~grid%2F2-Wide_Awning.jpg.thumbnail.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Picture/Exterior Finish/Frame Colour": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Picture%2F~grid%2FGWD_260A.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Picture/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Picture/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Picture/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency 400/Regency 400 Picture/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency 400/Regency 400 Picture/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency 400/Regency 400 Picture/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #
    #
    # "Window/categories/Regency 400/Regency 400 Slider/Configuration/2 Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FOX.png.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Configuration/2 Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FXO.png.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Configuration/Picture over 2 Lite - Left Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FP-OX.png.thumbnail.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Configuration/Picture over 2 Lite - Right Operating": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Sliding%2F~grid%2FP-XO.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Slider/Exterior Finish/Definity Vinyl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Sliding%2F~grid%2F20Series_DH.png.thumbnail.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/No Grilles": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNONE_thumb.jpg",
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/Flat": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FClassic.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/Euro Contoured": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/Simulated Divided Lites 1 1/4":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/Simulated Divided Lites 2": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FContoured.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/Rectangular Pewter": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FNarrow-Brass.png",
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Type/V-Grooved Cut Glass": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Casement%2F~grid%2FVGrooveCutGlassthumb.png",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Slider/Grille Style": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%20400%2F~Regency400_Sliding%2F~grid%2F0-NONE_thumb.jpg",
    #
    #
    # "Window/categories/Regency 400/Regency 400 Slider/Glass/Obscure": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fobscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Slider/Glass/Niagara": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Frain-obscure.jpg",
    # "Window/categories/Regency 400/Regency 400 Slider/Glass/Glue Chip": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fglue-chip.jpg",
    # "Window/categories/Regency 400/Regency 400 Slider/Glass/Satin": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fsatin-etched.jpg",
    # "Window/categories/Regency 400/Regency 400 Slider/Glass/Bronze Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fbronze.jpg",
    # "Window/categories/Regency 400/Regency 400 Slider/Glass/Gray Tint": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FWindows%2FRegency%2F~Regency_Awning%2F~grid%2Fgray.jpg",
    #
    #


}
