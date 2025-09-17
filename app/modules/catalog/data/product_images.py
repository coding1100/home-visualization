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
    "Wall/categories/Siding/Align":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    "Wall/categories/Siding/Aluminum":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    "Wall/categories/Siding/Steel":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    "Wall/categories/Siding/Vinyl":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    "Wall/categories/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",

    # --- Siding → Align (leaf items, by order) ---
    'Wall/categories/Siding/Align/Align 7" Plank':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Align/Align 12" Board and Batten Matte':       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Align/Align 12" Board and Batten Woodgrain':   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",

    # --- Siding → Aluminum (9 items, by order) ---
    "Wall/categories/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding':  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Aluminum/Longboard 4" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Aluminum/Longboard 6" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",

    # --- Siding → Steel (7 items, by order) ---
    "Wall/categories/Siding/Steel/Distinction Siding":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Steel/Sierra Steel 8" Clapboard':                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Steel/Sierra Steel D4 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Steel/Sierra Steel D5 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Steel/Steel Side D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Steel/Steel Side D5 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",

    # --- Siding → Vinyl (23 items, by order) ---
    "Wall/categories/Siding/Vinyl/Board and Batten":                           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Concord D4 Clapboard":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Concord D4 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Concord D5 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Driftwood II D4.5 Dutch Lap":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Driftwood II D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Fairhaven Sound Single Select Scallops":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Fairhaven Sound Single Select Shakes":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Fairweather Vertical":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Foundry FPX":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Perfection Shingle":                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Rounds":                                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Split Shake":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Vinyl/Staggered Shake 10"':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    'Wall/categories/Siding/Vinyl/Staggered Shake 7"':                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Oxford Premium":                              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Sequoia Select D4 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Sequoia Select D5 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Single Select Scallops":                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Vinyl/Single Select Shakes":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",

    # --- Siding → Specialty Siding (2 items, by order) ---
    "Wall/categories/Siding/Specialty Siding/ChamClad":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    "Wall/categories/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",

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
    "Accent/categories/Siding/Align": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    "Accent/categories/Siding/Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    "Accent/categories/Siding/Steel": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    "Accent/categories/Siding/Vinyl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    "Accent/categories/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",

    # --- Accent → Align (leaf items, by order) ---
    'Accent/categories/Siding/Align/Align 7" Plank': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Align/Align 12" Board and Batten Matte': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Align/Align 12" Board and Batten Woodgrain': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",

    # --- Accent → Aluminum (9 items, by order) ---
    "Accent/categories/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Aluminum/Longboard 4" V Groove': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Aluminum/Longboard 6" V Groove': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",

    # --- Accent → Steel (7 items, by order) ---
    "Accent/categories/Siding/Steel/Distinction Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Steel/Sierra Steel 8" Clapboard': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Steel/Sierra Steel D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Steel/Sierra Steel D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Steel/Steel Side D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Steel/Steel Side D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",

    # --- Accent → Vinyl (23 items, by order) ---
    "Accent/categories/Siding/Vinyl/Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Concord D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Concord D4 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Concord D5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Driftwood II D4.5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Driftwood II D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Fairhaven Sound Single Select Scallops": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Fairhaven Sound Single Select Shakes": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Fairweather Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Foundry FPX": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    "Accent/categories/categories/Siding/Vinyl/Perfection Shingle": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Rounds": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Split Shake": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Vinyl/Staggered Shake 10"': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    'Accent/categories/Siding/Vinyl/Staggered Shake 7"': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Oxford Premium": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Sequoia Select D4 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Sequoia Select D5 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Single Select Scallops": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Vinyl/Single Select Shakes": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",

    # --- Accent → Specialty Siding (2 items, by order) ---
    "Accent/categories/Siding/Specialty Siding/ChamClad": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    "Accent/categories/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",

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
    "Masonry/categories/Siding/Align":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2Flogo.png",
    "Masonry/categories/Siding/Aluminum":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2Flogo.png",
    "Masonry/categories/Siding/Steel":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2Flogo.png",
    "Masonry/categories/Siding/Vinyl":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2Flogo.png",
    "Masonry/categories/Siding/Specialty Siding": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2Flogo.png",

    # --- Siding → Align (leaf items, by order) ---
    'Masonry/categories/Siding/Align/Align 7" Plank':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Align/Align 12" Board and Batten Matte':       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Matte%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Align/Align 12" Board and Batten Woodgrain':   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAlign%2F~GentekCAN_Align%20BB%20Woodgrain%2F~swatch0-400.jpg",

    # --- Siding → Aluminum (9 items, by order) ---
    "Masonry/categories/Siding/Aluminum/Vertical V Woodgrain 2000 Aluminum":  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000Woodgrain_Vertical_V_Woodgrain%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Aluminum/8" Smooth - Deluxe Aluminum Siding':  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Aluminum2000_Smooth_8%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Aluminum/8" Woodgrain - 2000 Aluminum Siding': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_8%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Aluminum/D4 Clapboard - Woodgrain 2000 Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~AluminumWoodgrain2000_D4_Clapboard%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Aluminum/Longboard 4" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_4_VGroove%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Aluminum/Longboard 6" V Groove':               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Longboard_6_VGroove%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Aluminum/8" Board and Batten Smooth - Deluxe': "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_8_BoardandBatten%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Aluminum/D4 Clapboard - Smooth Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~SmoothDeluxeAluminum_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Aluminum/Vertical V Smooth - Deluxe Aluminum": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FAluminum%2F~Vertical_VSmooth_DeluxeAluminum%2F~swatch0-400.jpg",

    # --- Siding → Steel (7 items, by order) ---
    "Masonry/categories/Siding/Steel/Distinction Siding":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~DistinctionSiding%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Steel/Sierra Steel 8" Clapboard':                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_8_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Steel/Sierra Steel D4 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Steel/Sierra Steel D5 Clapboard":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_D5_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Steel/Sierra Steel S12 Vertical Board and Batten": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SierraSteel_S12_Vertical_BnB%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Steel/Steel Side D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Steel/Steel Side D5 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSteel%2F~SteelSide_D5_Clapboard%2F~swatch0-400.jpg",

    # --- Siding → Vinyl (23 items, by order) ---
    "Masonry/categories/Siding/Vinyl/Board and Batten":                           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~BoardandBatten%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Concord D4 Clapboard":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Concord D4 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D4_DutchLap%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Concord D5 Dutch Lap":                       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Concord_D5_DutchLap%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Driftwood II D4.5 Dutch Lap":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D45_DutchLap%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Driftwood II D4 Clapboard":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Driftwood_II_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Fairhaven Sound Single Select Scallops":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Scallops%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Fairhaven Sound Single Select Shakes":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FairhavenSound_Shakes%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Fairweather Vertical":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Fairweather_Vertical%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Foundry FPX":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryFPX%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Perfection Shingle":                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryPerfectionShingle%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Rounds":                                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryRounds%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Split Shake":                                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundrySplitShake%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Vinyl/Staggered Shake 10"':                         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_10in%2F~swatch0-400.jpg",
    'Masonry/categories/Siding/Vinyl/Staggered Shake 7"':                          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~FoundryStaggeredShake_7in%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Oxford Premium":                              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~OxfordPremium%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Sequoia Select D4.5 Dutch Lap":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D45_DutchLap_Grain%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Sequoia Select D4 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D4_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Sequoia Select D5 Clapboard":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_D5_Clapboard%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Sequoia Select Enfusion D5 Dutch Lap":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D5_DutchLap%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Sequoia Select Enfusion D6 Clapboard":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~SequoiaSelect_Enfusion_D6%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Single Select Scallops":                      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Scallops%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Vinyl/Single Select Shakes":                        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FVinyl%2F~Single_Select_Shakes%2F~swatch0-400.jpg",

    # --- Siding → Specialty Siding (2 items, by order) ---
    "Masonry/categories/Siding/Specialty Siding/ChamClad":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad%2F~swatch0-400.jpg",
    "Masonry/categories/Siding/Specialty Siding/ChamClad Vertical": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FSiding%2FSpecialty%20Siding%2F~ChamClad_Vertical%2F~swatch0-400.jpg",

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



    # Aluminum Trim & Accessories (logo)
    "Trim/Paint and Trim/Aluminum Trim and Accessories": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FTrim%2FAluminum%20Trim%20and%20Accessories%2Flogo.png",
    "Trim/Paint and Trim/Vinyl Trim and Accessories": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FTrim%2FVinyl%20Trim%20and%20Accessories%2Flogo.png",
    "Trim/Paint and Trim/Gentek Performance G8 Piece": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FTrim%2FGentek%20Performance%20G8%20Piece%2Flogo.png",


    # Aluminum Trim & Accessories
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Bright White":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch0-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Sandstone":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch1-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Cashmere":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch2-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Almond":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch3-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Maize":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch4-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Monterey Sand":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch5-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Cream":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch6-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Canyon Clay":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch7-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Wicker":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch8-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Pebble":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch9-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Brownstone":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch10-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Dover Gray":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch11-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Metallic Gray":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch12-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Sage":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch13-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Juniper Grove":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch14-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Storm":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch15-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Sable":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Windswept Smoke":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch17-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Midnight Surf":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch18-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Wedgewood Blue":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Rockwell Blue":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch20-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Coastal Blue":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch21-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Ivy Green":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Slate":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch23-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Dark Drift":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch24-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Espresso":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch25-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Moonlit Moss":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch26-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Chestnut Brown":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Commercial Brown":    "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch28-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Nutmeg":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Antique Brown":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Forest Green":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Graphite":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Iron Ore":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch33-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Black":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch34-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Chesapeake Gray":     "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Majestic Brick":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Rockport Brown":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Smoked Timber":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Meadow Fern":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Marine Dusk":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch40-400.jpg",
    "Trim/Paint and Trim/Aluminum Trim and Accessories/Hudson Slate":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch41-400.jpg",

    # Vinyl Trim & Accessories
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Almond":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch0-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Amber":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch1-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Canyon Clay":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch2-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Chesapeake Gray":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch3-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Coastal Blue":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch4-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Dark Drift":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch5-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Dover Gray":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch6-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Espresso":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch7-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Hudson Slate":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch8-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Iron Ore":               "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch9-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Juniper Grove":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch10-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Linen":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch11-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Maize":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch12-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Majestic Brick":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch13-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Marine Dusk":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch14-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Meadow Fern":            "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch15-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Midnight Surf":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Monteray Sand":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch17-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Moonlit Moss":           "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch18-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Pearl":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Pebble":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch20-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Rockport Brown":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch21-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Rockwell Blue":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Sage":                   "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch23-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Sandstone":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch24-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Smoked Timber":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch25-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Snow White":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch26-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Storm":                  "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Wicker":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch28-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Windswept Smoke":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/BarnBoard Grey":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Honey Super Matte":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Super Matte Modern Walnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Sun Bleached Oak":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch33-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Cinnamon Walnut":        "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch34-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Barrel Oak":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Toffee":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Charred Black":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Atlantic White":         "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Chai Cedar":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Brushed Metallic":       "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch40-400.jpg",
    "Trim/Paint and Trim/Vinyl Trim and Accessories/Pure White":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch41-400.jpg",

    # Gentek Performance G8 Piece
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Ice White":             "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch0-400.jpg",
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Bright White":          "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch1-400.jpg",
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Pebble":                "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch2-400.jpg",
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Commercial Brown":      "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch3-400.jpg",
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Slate":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch4-400.jpg",
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Iron Ore":              "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch5-400.jpg",
    "Trim/Paint and Trim/Gentek Performance G8 Piece/Black":                 "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch6-400.jpg",








    # Aluminum Trim & Accessories (logo)
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Bright White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch0-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Sandstone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch1-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Cashmere": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch2-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Almond": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch3-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Maize": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch4-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Monterey Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch5-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Cream": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch6-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Canyon Clay": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch7-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Wicker": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch8-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Pebble": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch9-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Brownstone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch10-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Dover Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch11-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Metallic Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch12-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Sage": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch13-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Juniper Grove": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch14-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Storm": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch15-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Sable": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Windswept Smoke": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch17-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Midnight Surf": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch18-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Wedgewood Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Rockwell Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch20-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Coastal Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch21-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Ivy Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch23-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Dark Drift": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch24-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Espresso": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch25-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Moonlit Moss": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch26-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Chestnut Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Commercial Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch28-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Nutmeg": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Antique Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Forest Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Graphite": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Iron Ore": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch33-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch34-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Chesapeake Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Majestic Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Rockport Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Smoked Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Meadow Fern": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Marine Dusk": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch40-400.jpg",
    "Window and Door Trim/Paint and Trim/Aluminum Trim and Accessories/Hudson Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Alum%20Trim%20and%20Access%2F~swatch41-400.jpg",

    # Vinyl Trim & Accessories
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Almond": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch0-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Amber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch1-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Canyon Clay": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch2-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Chesapeake Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch3-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Coastal Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch4-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Dark Drift": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch5-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Dover Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch6-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Espresso": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch7-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Hudson Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch8-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Iron Ore": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch9-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Juniper Grove": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch10-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Linen": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch11-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Maize": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch12-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Majestic Brick": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch13-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Marine Dusk": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch14-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Meadow Fern": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch15-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Midnight Surf": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch16-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Monteray Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch17-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Moonlit Moss": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch18-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Pearl": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch19-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Pebble": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch20-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Rockport Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch21-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Rockwell Blue": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch22-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Sage": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch23-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Sandstone": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch24-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Smoked Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch25-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Snow White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch26-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Storm": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch27-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Wicker": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch28-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Windswept Smoke": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch29-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/BarnBoard Grey": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch30-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Honey Super Matte": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch31-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Super Matte Modern Walnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch32-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Sun Bleached Oak": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch33-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Cinnamon Walnut": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch34-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Barrel Oak": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch35-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Toffee": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch36-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Charred Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch37-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Atlantic White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch38-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Chai Cedar": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch39-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Brushed Metallic": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch40-400.jpg",
    "Window and Door Trim/Paint and Trim/Vinyl Trim and Accessories/Pure White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Vinyl%20Trim%20and%20Access%2F~swatch41-400.jpg",

    # Gentek Performance G8 Piece
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Ice White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch0-400.jpg",
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Bright White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch1-400.jpg",
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Pebble": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch2-400.jpg",
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Commercial Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch3-400.jpg",
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch4-400.jpg",
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Iron Ore": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch5-400.jpg",
    "Window and Door Trim/Paint and Trim/Gentek Performance G8 Piece/Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FPaint%20and%20Trim%2F~Gentek%20001%20Performance%20G8%20Piece%2F~swatch6-400.jpg",

    # -------------------- ROOFING / GAF --------------------

    # 3-Tab (group + series logos)
    "Roofing/GAF/3-Tab": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2Flogo.png",
    "Roofing/GAF/3-Tab/Marquis Weathermax": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2Flogo.png",
    "Roofing/GAF/3-Tab/Royal Sovereign": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2Flogo.png",

    # 3-Tab / Marquis Weathermax® (swatches)
    "Roofing/GAF/3-Tab/Marquis Weathermax/Autumn Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2F~swatch0-400.jpg",
    "Roofing/GAF/3-Tab/Marquis Weathermax/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2F~swatch1-400.jpg",
    "Roofing/GAF/3-Tab/Marquis Weathermax/Weathered Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~MarquisWeathermax%2F~swatch2-400.jpg",

    # 3-Tab / Royal Sovereign® (swatches)
    "Roofing/GAF/3-Tab/Royal Sovereign/Ash Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch0-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Silver Lining": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch1-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch2-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Summer Sage": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch3-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/White": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch4-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Weathered Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch5-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Autumn Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch6-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch7-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Cypress Tan": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch8-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Golden Cedar": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch9-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Nickel Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch10-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Russet Red": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch11-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Sandrift": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch12-400.jpg",
    "Roofing/GAF/3-Tab/Royal Sovereign/Desert Sand": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2F3-Tab%2F~RoyalSovereign%2F~swatch13-400.jpg",

    # Designer (series logos)
    "Roofing/GAF/Designer/Camelot II": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2Flogo.png",
    "Roofing/GAF/Designer/Glenwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2Flogo.png",
    "Roofing/GAF/Designer/Grand Canyon": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2Flogo.png",
    "Roofing/GAF/Designer/Grand Sequoia": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2Flogo.png",
    "Roofing/GAF/Designer/Grand Sequoia AS": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2Flogo.png",
    "Roofing/GAF/Designer/Grand Sequoia RS": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2Flogo.png",
    "Roofing/GAF/Designer/Grand Sequoia RS+": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRSPlus%2Flogo.png",
    "Roofing/GAF/Designer/Slateline": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2Flogo.png",
    "Roofing/GAF/Designer/Woodland": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2Flogo.png",

    # Designer / Camelot II (swatches)
    "Roofing/GAF/Designer/Camelot II/Barkwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Camelot II/Weathered Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Camelot II/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Camelot II/Antique Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch3-400.jpg",
    "Roofing/GAF/Designer/Camelot II/Royal Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch4-400.jpg",
    "Roofing/GAF/Designer/Camelot II/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Camelot_II%2F~swatch5-400.jpg",

    # Designer / Glenwood® (swatches)
    "Roofing/GAF/Designer/Glenwood/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Glenwood/Golden Prairie": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Glenwood/Autumn Harvest": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Glenwood/Dusky Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch3-400.jpg",
    "Roofing/GAF/Designer/Glenwood/Adobe Clay": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch4-400.jpg",
    "Roofing/GAF/Designer/Glenwood/Chelsea Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Glenwood%2F~swatch5-400.jpg",

    # Designer / Grand Canyon™ (swatches)
    "Roofing/GAF/Designer/Grand Canyon/Stonewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Grand Canyon/Black Oak": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Grand Canyon/Mission Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Grand Canyon/Storm Cloud": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch3-400.jpg",
    "Roofing/GAF/Designer/Grand Canyon/Sedona Sunset": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandCanyon%2F~swatch4-400.jpg",

    # Designer / Grand Sequoia® (swatches)
    "Roofing/GAF/Designer/Grand Sequoia/Autumn Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia/Cedar": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia/Mesa Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch3-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia/Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch4-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia/Weathered Timber": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch5-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoia%2F~swatch6-400.jpg",

    # Designer / Grand Sequoia® AS (swatches)
    "Roofing/GAF/Designer/Grand Sequoia AS/Adobe Sunset": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia AS/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia AS/Dusky Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia AS/Weathered Wood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaAS%2F~swatch3-400.jpg",

    # Designer / Grand Sequoia® RS (swatches)
    "Roofing/GAF/Designer/Grand Sequoia RS/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia RS/Forest Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia RS/Ocean Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia RS/Sagewood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch3-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia RS/Sandalwood": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRS%2F~swatch4-400.jpg",

    # Designer / Grand Sequoia® RS+ (swatches)
    "Roofing/GAF/Designer/Grand Sequoia RS+/Charcoal": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRSPlus%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Grand Sequoia RS+/Forest Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~GrandSequoiaRSPlus%2F~swatch1-400.jpg",

    # Designer / Slateline® (swatches)
    "Roofing/GAF/Designer/Slateline/Antique Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch0-400.jpg",
    "Roofing/GAF/Designer/Slateline/Emerald Green": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch1-400.jpg",
    "Roofing/GAF/Designer/Slateline/English Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch2-400.jpg",
    "Roofing/GAF/Designer/Slateline/Royal Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch3-400.jpg",
    "Roofing/GAF/Designer/Slateline/Weathered Slate": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Slateline%2F~swatch4-400.jpg",

    # Designer / Woodland (swatches)
    "Roofing/GAF/Designer/Woodland/Castlewood Gray": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch0-400.jpg",
    "Roofing/categories/GAF/Designer/Woodland/Cedarwood Abbey": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch1-400.jpg",
    "Roofing/categories/GAF/Designer/Woodland/Tuscan Sunset": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch2-400.jpg",
    "Roofing/categories/GAF/Designer/Woodland/Woodberry Brown": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch3-400.jpg",
    "Roofing/categories/GAF/Designer/Woodland/Canterbury Black": "https://rw-product-bucket.renoworks.com/gentekcanada/70876%2FExterior%2FRoofing%2FGAF%2FDesigner%2F~Woodland%2F~swatch4-400.jpg",


}
