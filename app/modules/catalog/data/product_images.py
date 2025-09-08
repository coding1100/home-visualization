# app/modules/catalog/data/product_images.py

PRODUCT_IMAGE_MAP: dict[str, str] = {
    # === Wall → Categories (you already tested these) ===
    "Wall/categories/Brick":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2Flogo.png",
    "Wall/categories/Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    "Wall/categories/Stone":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2Flogo.png",

    # === Wall → Brick (leaf items, mapped by order) ===
    "Wall/categories/Brick/Red":                   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch0-400.jpg",
    "Wall/categories/Brick/Sand":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch1-400.jpg",
    "Wall/categories/Brick/Deep Red Handmould":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch2-400.jpg",
    "Wall/categories/Brick/Sand Rumbled":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch3-400.jpg",
    "Wall/categories/Brick/Cream Rockface":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch4-400.jpg",
    "Wall/categories/Brick/Dutch Molde":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch5-400.jpg",
    "Wall/categories/Brick/Charcoal":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch6-400.jpg",
    "Wall/categories/Brick/Cerise 1/3 Bond":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch7-400.jpg",
    "Wall/categories/Brick/Durham Rumbled":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch8-400.jpg",
    "Wall/categories/Brick/Silver":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch9-400.jpg",
    "Wall/categories/Brick/Firerock King 1/3":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch10-400.jpg",
    "Wall/categories/Brick/Mute Red":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch11-400.jpg",
    "Wall/categories/Brick/Crimson":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch12-400.jpg",

    # === Wall → Siding (sub-category logos) ===
    "Wall/Siding/Align":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    "Wall/Siding/Aluminum":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    "Wall/Siding/Steel":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    "Wall/Siding/Vinyl":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    "Wall/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",

    # --- Siding → Align (leaf items, by order) ---
    'Wall/Siding/Align/Align 7" Plank':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    'Wall/Siding/Align/Align 12" Board and Batten Matte':       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    'Wall/Siding/Align/Align 12" Board and Batten Woodgrain':   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",

    # --- Siding → Aluminum (9 items, by order) ---
    "Wall/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    'Wall/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding':  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    'Wall/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    "Wall/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    'Wall/Siding/Aluminum/Longboard 4" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    'Wall/Siding/Aluminum/Longboard 6" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    'Wall/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    "Wall/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",

    # --- Siding → Steel (7 items, by order) ---
    "Wall/Siding/Steel/Distinction Siding":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    'Wall/Siding/Steel/Sierra Steel 8" Clapboard':                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Steel/Sierra Steel D4 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Steel/Sierra Steel D5 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    "Wall/Siding/Steel/Steel Side D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Steel/Steel Side D5 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",

    # --- Siding → Vinyl (23 items, by order) ---
    "Wall/Siding/Vinyl/Board and Batten":                           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Concord D4 Clapboard":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Concord D4 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Concord D5 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Driftwood II D4.5 Dutch Lap":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Driftwood II D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Fairhaven Sound Single Select Scallops":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Fairhaven Sound Single Select Shakes":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Fairweather Vertical":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Foundry FPX":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Perfection Shingle":                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Rounds":                                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Split Shake":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    'Wall/Siding/Vinyl/Staggered Shake 10"':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    'Wall/Siding/Vinyl/Staggered Shake 7"':                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Oxford Premium":                              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Sequoia Select D4 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Sequoia Select D5 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Single Select Scallops":                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    "Wall/Siding/Vinyl/Single Select Shakes":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",

    # --- Siding → Specialty Siding (2 items, by order) ---
    "Wall/Siding/Specialty Siding/ChamClad":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    "Wall/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",

    # === Wall → Stone (brand logos) ===
    "Wall/categories/Stone/Foundry":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2Flogo.png",
    "Wall/categories/Stone/Gentek Canada": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2Flogo.png",

    # --- Stone → Foundry (4 items, by order) ---
    "Wall/categories/Stone/Foundry/Cottonwood":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch0-400.jpg",
    "Wall/categories/Stone/Foundry/Desert Canyon":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch1-400.jpg",
    "Wall/categories/Stone/Foundry/Mesa":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch2-400.jpg",
    "Wall/categories/Stone/Foundry/Red Rock":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch3-400.jpg",

    # --- Stone → Gentek Canada (series-level images; colors below will stay null unless provided) ---
    "Wall/categories/Stone/Gentek Canada/Carved Block": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    "Wall/categories/Stone/Gentek Canada/Ledgestone":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_Ledgestone%2F~swatch0-400.jpg",
    "Wall/categories/Stone/Gentek Canada/Tight Cut":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",

    # === Accent → Categories (you already tested these) ===
    "Accent/categories/Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2Flogo.png",
    "Accent/categories/Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    "Accent/categories/Stone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2Flogo.png",

    # === Accent → Brick (leaf items, mapped by order) ===
    "Accent/categories/Brick/Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch0-400.jpg",
    "Accent/categories/Brick/Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch1-400.jpg",
    "Accent/categories/Brick/Deep Red Handmould": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch2-400.jpg",
    "Accent/categories/Brick/Sand Rumbled": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch3-400.jpg",
    "Accent/categories/Brick/Cream Rockface": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch4-400.jpg",
    "Accent/categories/Brick/Dutch Molde": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch5-400.jpg",
    "Accent/categories/Brick/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch6-400.jpg",
    "Accent/categories/Brick/Cerise 1/3 Bond": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch7-400.jpg",
    "Accent/categories/Brick/Durham Rumbled": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch8-400.jpg",
    "Accent/categories/Brick/Silver": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch9-400.jpg",
    "Accent/categories/Brick/Firerock King 1/3": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch10-400.jpg",
    "Accent/categories/Brick/Mute Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch11-400.jpg",
    "Accent/categories/Brick/Crimson": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch12-400.jpg",

    # === Accent → Siding (sub-category logos) ===
    "Accent/Siding/Align": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    "Accent/Siding/Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    "Accent/Siding/Steel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    "Accent/Siding/Vinyl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    "Accent/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",

    # --- Accent → Align (leaf items, by order) ---
    'Accent/Siding/Align/Align 7" Plank': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    'Accent/Siding/Align/Align 12" Board and Batten Matte': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    'Accent/Siding/Align/Align 12" Board and Batten Woodgrain': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",

    # --- Accent → Aluminum (9 items, by order) ---
    "Accent/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    'Accent/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    'Accent/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    "Accent/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    'Accent/Siding/Aluminum/Longboard 4" V Groove': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    'Accent/Siding/Aluminum/Longboard 6" V Groove': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    'Accent/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    "Accent/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",

    # --- Accent → Steel (7 items, by order) ---
    "Accent/Siding/Steel/Distinction Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    'Accent/Siding/Steel/Sierra Steel 8" Clapboard': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Steel/Sierra Steel D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Steel/Sierra Steel D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    "Accent/Siding/Steel/Steel Side D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Steel/Steel Side D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",

    # --- Accent → Vinyl (23 items, by order) ---
    "Accent/Siding/Vinyl/Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Concord D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Concord D4 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Concord D5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Driftwood II D4.5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Driftwood II D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Fairhaven Sound Single Select Scallops": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Fairhaven Sound Single Select Shakes": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Fairweather Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Foundry FPX": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Perfection Shingle": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Rounds": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Split Shake": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    'Accent/Siding/Vinyl/Staggered Shake 10"': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    'Accent/Siding/Vinyl/Staggered Shake 7"': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Oxford Premium": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Sequoia Select D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Sequoia Select D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Single Select Scallops": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    "Accent/Siding/Vinyl/Single Select Shakes": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",

    # --- Accent → Specialty Siding (2 items, by order) ---
    "Accent/Siding/Specialty Siding/ChamClad": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    "Accent/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",

    # === Accent → Stone (brand logos) ===
    "Accent/categories/Stone/Foundry": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2Flogo.png",
    "Accent/categories/Stone/Gentek Canada": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2Flogo.png",

    # --- Accent → Foundry (4 items, by order) ---
    "Accent/categories/Stone/Foundry/Cottonwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch0-400.jpg",
    "Accent/categories/Stone/Foundry/Desert Canyon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch1-400.jpg",
    "Accent/categories/Stone/Foundry/Mesa": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch2-400.jpg",
    "Accent/categories/Stone/Foundry/Red Rock": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch3-400.jpg",

    # --- Accent → Gentek Canada (series-level images; colors below will stay null unless provided) ---
    "Accent/categories/Stone/Gentek Canada/Carved Block": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    "Accent/categories/Stone/Gentek Canada/Ledgestone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_Ledgestone%2F~swatch0-400.jpg",
    "Accent/categories/Stone/Gentek Canada/Tight Cut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",



# === Masonry → Categories (you already tested these) ===
    "Masonry/categories/Brick":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2Flogo.png",
    "Masonry/categories/Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2Flogo.png",
    "Masonry/categories/Stone":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2Flogo.png",

    # === Masonry → Brick (leaf items, mapped by order) ===
    "Masonry/categories/Brick/Red":                   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch0-400.jpg",
    "Masonry/categories/Brick/Sand":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch1-400.jpg",
    "Masonry/categories/Brick/Deep Red Handmould":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch2-400.jpg",
    "Masonry/categories/Brick/Sand Rumbled":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch3-400.jpg",
    "Masonry/categories/Brick/Cream Rockface":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch4-400.jpg",
    "Masonry/categories/Brick/Dutch Molde":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch5-400.jpg",
    "Masonry/categories/Brick/Charcoal":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch6-400.jpg",
    "Masonry/categories/Brick/Cerise 1/3 Bond":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch7-400.jpg",
    "Masonry/categories/Brick/Durham Rumbled":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch8-400.jpg",
    "Masonry/categories/Brick/Silver":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch9-400.jpg",
    "Masonry/categories/Brick/Firerock King 1/3":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch10-400.jpg",
    "Masonry/categories/Brick/Mute Red":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch11-400.jpg",
    "Masonry/categories/Brick/Crimson":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FBrick%2F~generic_brick%2F~swatch12-400.jpg",

    # === Masonry → Siding (sub-category logos) ===
    "Masonry/Siding/Align":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    "Masonry/Siding/Aluminum":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    "Masonry/Siding/Steel":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    "Masonry/Siding/Vinyl":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    "Masonry/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",

    # --- Siding → Align (leaf items, by order) ---
    'Masonry/Siding/Align/Align 7" Plank':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    'Masonry/Siding/Align/Align 12" Board and Batten Matte':       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    'Masonry/Siding/Align/Align 12" Board and Batten Woodgrain':   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",

    # --- Siding → Aluminum (9 items, by order) ---
    "Masonry/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    'Masonry/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding':  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    'Masonry/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    "Masonry/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    'Masonry/Siding/Aluminum/Longboard 4" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    'Masonry/Siding/Aluminum/Longboard 6" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    'Masonry/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    "Masonry/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",

    # --- Siding → Steel (7 items, by order) ---
    "Masonry/Siding/Steel/Distinction Siding":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    'Masonry/Siding/Steel/Sierra Steel 8" Clapboard':                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Steel/Sierra Steel D4 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Steel/Sierra Steel D5 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    "Masonry/Siding/Steel/Steel Side D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Steel/Steel Side D5 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",

    # --- Siding → Vinyl (23 items, by order) ---
    "Masonry/Siding/Vinyl/Board and Batten":                           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Concord D4 Clapboard":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Concord D4 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Concord D5 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Driftwood II D4.5 Dutch Lap":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Driftwood II D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Fairhaven Sound Single Select Scallops":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Fairhaven Sound Single Select Shakes":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Fairweather Vertical":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Foundry FPX":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Perfection Shingle":                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Rounds":                                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Split Shake":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    'Masonry/Siding/Vinyl/Staggered Shake 10"':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    'Masonry/Siding/Vinyl/Staggered Shake 7"':                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Oxford Premium":                              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Sequoia Select D4 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Sequoia Select D5 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Single Select Scallops":                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    "Masonry/Siding/Vinyl/Single Select Shakes":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",

    # --- Siding → Specialty Siding (2 items, by order) ---
    "Masonry/Siding/Specialty Siding/ChamClad":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    "Masonry/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",

    # === Wall → Stone (brand logos) ===
    "Masonry/categories/Stone/Foundry":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2Flogo.png",
    "Masonry/categories/Stone/Gentek Canada": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2Flogo.png",

    # --- Stone → Foundry (4 items, by order) ---
    "Masonry/categories/Stone/Foundry/Cottonwood":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch0-400.jpg",
    "Masonry/categories/Stone/Foundry/Desert Canyon":"https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch1-400.jpg",
    "Masonry/categories/Stone/Foundry/Mesa":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch2-400.jpg",
    "Masonry/categories/Stone/Foundry/Red Rock":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FFoundry%2F~FoundryLimestone%2F~swatch3-400.jpg",

    # --- Stone → Gentek Canada (series-level images; colors below will stay null unless provided) ---
    "Masonry/categories/Stone/Gentek Canada/Carved Block": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_CarvedBlock%2F~swatch0-400.jpg",
    "Masonry/categories/Stone/Gentek Canada/Ledgestone":   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_Ledgestone%2F~swatch0-400.jpg",
    "Masonry/categories/Stone/Gentek Canada/Tight Cut":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FStone%2FGentek%20Canada%2FVersetta%20Stone%2F~Boral_Versetta_Stone_TightCut%2F~swatch0-400.jpg",

}
