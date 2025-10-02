# app/modules/catalog/data/products_data.py

from __future__ import annotations
from typing import Dict, List, Union

# A node is either a list of leaf items (List[str]) or another nested mapping (Dict[str, Node])
Node = Union[List[str], Dict[str, "Node"]]

PRODUCTS_DATA: Dict[str, Dict[str, Node]] = {
    # 1) WALL
    "Wall": {
        "categories": {
            # --- Brick
            # "Brick": [
            #     "Red",
            #     "Sand",
            #     "Deep Red Handmould",
            #     "Sand Rumbled",
            #     "Cream Rockface",
            #     "Dutch Molde",
            #     "Charcoal",
            #     "Cerise 1/3 Bond",
            #     "Durham Rumbled",
            #     "Silver",
            #     "Firerock King 1/3",
            #     "Mute Red",
            #     "Crimson",
            # ],
            #
            #
            # "Premium Composite Siding": [
            #     "Board and batten",
            #     "Lap",
            #
            # ],
            #
            # # --- Siding (with sub-families)
            # "Siding": {
            #     "Align": [
            #         "Align 7\" Plank",
            #         "Align 12\" Board and Batten Matte",
            #         "Align 12\" Board and Batten Woodgrain",
            #     ],
            #     "Aluminum": [
            #         "Vertical V Woodgrain 2000 Aluminum",
            #         "8\" Smooth - Deluxe Aluminum Siding",
            #         "8\" Woodgrain - 2000 Aluminum Siding",
            #         "D4 Clapboard - Woodgrain 2000 Aluminum",
            #         "Longboard 4\" V Groove",
            #         "Longboard 6\" V Groove",
            #         "8\" Board and Batten Smooth - Deluxe",
            #         "D4 Clapboard - Smooth Deluxe Aluminum",
            #         "Vertical V Smooth - Deluxe Aluminum",
            #     ],
            #     "Steel": [
            #         "Distinction Siding",
            #         "Sierra Steel 8\" Clapboard",
            #         "Sierra Steel D4 Clapboard",
            #         "Sierra Steel D5 Clapboard",
            #         "Sierra Steel S12 Vertical Board and Batten",
            #         "Steel Side D4 Clapboard",
            #         "Steel Side D5 Clapboard",
            #     ],
            #     "Vinyl": [
            #         "Board and Batten",
            #         "Concord D4 Clapboard",
            #         "Concord D4 Dutch Lap",
            #         "Concord D5 Dutch Lap",
            #         "Driftwood II D4.5 Dutch Lap",
            #         "Driftwood II D4 Clapboard",
            #         "Fairhaven Sound Single Select Scallops",
            #         "Fairhaven Sound Single Select Shakes",
            #         "Fairweather Vertical",
            #         "Foundry FPX",
            #         "Perfection Shingle",
            #         "Rounds",
            #         "Split Shake",
            #         "Staggered Shake 10\"",
            #         "Staggered Shake 7\"",
            #         "Oxford Premium",
            #         "Sequoia Select D4.5 Dutch Lap",
            #         "Sequoia Select D4 Clapboard",
            #         "Sequoia Select D5 Clapboard",
            #         "Sequoia Select Enfusion D5 Dutch Lap",
            #         "Sequoia Select Enfusion D6 Clapboard",
            #         "Single Select Scallops",
            #         "Single Select Shakes",
            #     ],
            #     "Specialty Siding": [
            #         "ChamClad",
            #         "ChamClad Vertical",
            #     ],
            # },
            #
            # # --- Stone (with brands and series)
            # "Stone": {
            #     "Foundry": [
            #         "Cottonwood",
            #         "Desert Canyon",
            #         "Mesa",
            #         "Red Rock",
            #     ],
            #     "Gentek Canada": {
            #         "Carved Block": [
            #             "Midnight",
            #             "Sea Salt",
            #         ],
            #         "Ledgestone": [
            #             "Mission Point",
            #             "Plum Creek",
            #             "Sterling",
            #             "Terra Rosa",
            #             "Sand",
            #             "Northern Ash",
            #         ],
            #         "Tight Cut": [
            #             "Mission Point",
            #             "Plum Creek",
            #             "Sterling",
            #             "Terra Rosa",
            #             "Sand",
            #             "Northern Ash",
            #         ],
            #     },
            # },
"Premium Composite Siding": {
      "Board and batten": [
        "Artic Blue",
        "Bourbon",
        "Brickstone Red",
        "Cashmere",
        "Charcoal",
        "Forest",
        "Khaki",
        "Midnight",
        "Ocean Mist",
        "Polar White",
        "Saddle Brown",
        "Sage",
        "Sand Dune",
        "Sea Moss",
        "Smoke Grey"
      ],
      "Lap Siding": [
        "Bourbon",
        "Charcoal",
        "Khaki",
        "Midnight",
        "Ocean Mist",
        "Polar White",
        "Saddle Brown",
        "Sand Dune",
        "Sea Moss",
        "Smoke Grey",
        "Artic Blue",
        "Brickstone Red",
        "Cashmere",
        "Forest",
        "Sage"
      ]
    }
        }
    },

    # 2) ACCENT (placeholder for now)
    "Accent": {
        "categories": {
        #     # --- Brick
        #     "Brick": [
        #         "Red",
        #         "Sand",
        #         "Deep Red Handmould",
        #         "Sand Rumbled",
        #         "Cream Rockface",
        #         "Dutch Molde",
        #         "Charcoal",
        #         "Cerise 1/3 Bond",
        #         "Durham Rumbled",
        #         "Silver",
        #         "Firerock King 1/3",
        #         "Mute Red",
        #         "Crimson",
        #     ],
        #
        #     # --- Siding (with sub-families)
        #     "Siding": {
        #         "Align": [
        #             "Align 7\" Plank",
        #             "Align 12\" Board and Batten Matte",
        #             "Align 12\" Board and Batten Woodgrain",
        #         ],
        #         "Aluminum": [
        #             "Vertical V Woodgrain 2000 Aluminum",
        #             "8\" Smooth - Deluxe Aluminum Siding",
        #             "8\" Woodgrain - 2000 Aluminum Siding",
        #             "D4 Clapboard - Woodgrain 2000 Aluminum",
        #             "Longboard 4\" V Groove",
        #             "Longboard 6\" V Groove",
        #             "8\" Board and Batten Smooth - Deluxe",
        #             "D4 Clapboard - Smooth Deluxe Aluminum",
        #             "Vertical V Smooth - Deluxe Aluminum",
        #         ],
        #         "Steel": [
        #             "Distinction Siding",
        #             "Sierra Steel 8\" Clapboard",
        #             "Sierra Steel D4 Clapboard",
        #             "Sierra Steel D5 Clapboard",
        #             "Sierra Steel S12 Vertical Board and Batten",
        #             "Steel Side D4 Clapboard",
        #             "Steel Side D5 Clapboard",
        #         ],
        #         "Vinyl": [
        #             "Board and Batten",
        #             "Concord D4 Clapboard",
        #             "Concord D4 Dutch Lap",
        #             "Concord D5 Dutch Lap",
        #             "Driftwood II D4.5 Dutch Lap",
        #             "Driftwood II D4 Clapboard",
        #             "Fairhaven Sound Single Select Scallops",
        #             "Fairhaven Sound Single Select Shakes",
        #             "Fairweather Vertical",
        #             "Foundry FPX",
        #             "Perfection Shingle",
        #             "Rounds",
        #             "Split Shake",
        #             "Staggered Shake 10\"",
        #             "Staggered Shake 7\"",
        #             "Oxford Premium",
        #             "Sequoia Select D4.5 Dutch Lap",
        #             "Sequoia Select D4 Clapboard",
        #             "Sequoia Select D5 Clapboard",
        #             "Sequoia Select Enfusion D5 Dutch Lap",
        #             "Sequoia Select Enfusion D6 Clapboard",
        #             "Single Select Scallops",
        #             "Single Select Shakes",
        #         ],
        #         "Specialty Siding": [
        #             "ChamClad",
        #             "ChamClad Vertical",
        #         ],
        #     },
        #
        #     # --- Stone (with brands and series)
        #     "Stone": {
        #         "Foundry": [
        #             "Cottonwood",
        #             "Desert Canyon",
        #             "Mesa",
        #             "Red Rock",
        #         ],
        #         "Gentek Canada": {
        #             "Carved Block": [
        #                 "Midnight",
        #                 "Sea Salt",
        #             ],
        #             "Ledgestone": [
        #                 "Mission Point",
        #                 "Plum Creek",
        #                 "Sterling",
        #                 "Terra Rosa",
        #                 "Sand",
        #                 "Northern Ash",
        #             ],
        #             "Tight Cut": [
        #                 "Mission Point",
        #                 "Plum Creek",
        #                 "Sterling",
        #                 "Terra Rosa",
        #                 "Sand",
        #                 "Northern Ash",
        #             ],
        #         },
        #     },
"Premium Composite Siding": {
      "Board and batten": [
        "Artic Blue",
        "Bourbon",
        "Brickstone Red",
        "Cashmere",
        "Charcoal",
        "Forest",
        "Khaki",
        "Midnight",
        "Ocean Mist",
        "Polar White",
        "Saddle Brown",
        "Sage",
        "Sand Dune",
        "Sea Moss",
        "Smoke Grey"
      ],
      "Lap Siding": [
        "Bourbon",
        "Charcoal",
        "Khaki",
        "Midnight",
        "Ocean Mist",
        "Polar White",
        "Saddle Brown",
        "Sand Dune",
        "Sea Moss",
        "Smoke Grey",
        "Artic Blue",
        "Brickstone Red",
        "Cashmere",
        "Forest",
        "Sage"
      ]
    }
        }
    },

    # 3) MASONRY
    # "Masonry": {
    #     "categories": {
    #         # --- Brick
    #         "Brick": [
    #             "Red",
    #             "Sand",
    #             "Deep Red Handmould",
    #             "Sand Rumbled",
    #             "Cream Rockface",
    #             "Dutch Molde",
    #             "Charcoal",
    #             "Cerise 1/3 Bond",
    #             "Durham Rumbled",
    #             "Silver",
    #             "Firerock King 1/3",
    #             "Mute Red",
    #             "Crimson",
    #         ],
    #
    #         # --- Siding (with sub-families)
    #         "Siding": {
    #             "Align": [
    #                 "Align 7\" Plank",
    #                 "Align 12\" Board and Batten Matte",
    #                 "Align 12\" Board and Batten Woodgrain",
    #             ],
    #             "Aluminum": [
    #                 "Vertical V Woodgrain 2000 Aluminum",
    #                 "8\" Smooth - Deluxe Aluminum Siding",
    #                 "8\" Woodgrain - 2000 Aluminum Siding",
    #                 "D4 Clapboard - Woodgrain 2000 Aluminum",
    #                 "Longboard 4\" V Groove",
    #                 "Longboard 6\" V Groove",
    #                 "8\" Board and Batten Smooth - Deluxe",
    #                 "D4 Clapboard - Smooth Deluxe Aluminum",
    #                 "Vertical V Smooth - Deluxe Aluminum",
    #             ],
    #             "Steel": [
    #                 "Distinction Siding",
    #                 "Sierra Steel 8\" Clapboard",
    #                 "Sierra Steel D4 Clapboard",
    #                 "Sierra Steel D5 Clapboard",
    #                 "Sierra Steel S12 Vertical Board and Batten",
    #                 "Steel Side D4 Clapboard",
    #                 "Steel Side D5 Clapboard",
    #             ],
    #             "Vinyl": [
    #                 "Board and Batten",
    #                 "Concord D4 Clapboard",
    #                 "Concord D4 Dutch Lap",
    #                 "Concord D5 Dutch Lap",
    #                 "Driftwood II D4.5 Dutch Lap",
    #                 "Driftwood II D4 Clapboard",
    #                 "Fairhaven Sound Single Select Scallops",
    #                 "Fairhaven Sound Single Select Shakes",
    #                 "Fairweather Vertical",
    #                 "Foundry FPX",
    #                 "Perfection Shingle",
    #                 "Rounds",
    #                 "Split Shake",
    #                 "Staggered Shake 10\"",
    #                 "Staggered Shake 7\"",
    #                 "Oxford Premium",
    #                 "Sequoia Select D4.5 Dutch Lap",
    #                 "Sequoia Select D4 Clapboard",
    #                 "Sequoia Select D5 Clapboard",
    #                 "Sequoia Select Enfusion D5 Dutch Lap",
    #                 "Sequoia Select Enfusion D6 Clapboard",
    #                 "Single Select Scallops",
    #                 "Single Select Shakes",
    #             ],
    #             "Specialty Siding": [
    #                 "ChamClad",
    #                 "ChamClad Vertical",
    #             ],
    #         },
    #
    #         # --- Stone (with brands and series)
    #         "Stone": {
    #             "Foundry": [
    #                 "Cottonwood",
    #                 "Desert Canyon",
    #                 "Mesa",
    #                 "Red Rock",
    #             ],
    #             "Gentek Canada": {
    #                 "Carved Block": [
    #                     "Midnight",
    #                     "Sea Salt",
    #                 ],
    #                 "Ledgestone": [
    #                     "Mission Point",
    #                     "Plum Creek",
    #                     "Sterling",
    #                     "Terra Rosa",
    #                     "Sand",
    #                     "Northern Ash",
    #                 ],
    #                 "Tight Cut": [
    #                     "Mission Point",
    #                     "Plum Creek",
    #                     "Sterling",
    #                     "Terra Rosa",
    #                     "Sand",
    #                     "Northern Ash",
    #                 ],
    #             },
    #         },
    #     }
    # },

    # 4) ROOFING
    # "Roof": {
    #     "categories": {
    #             "Timberline Roofing Shingles": {
    #                 "Timberline AH": [
    #                     "Amber Wheat", "Appalachian Sky", "Golden Harvest", "Cedar Falls",
    #                     "Midnight Blush", "Adobe Sunset", "Brandywine Dusk",
    #                     "Nantucket Morning", "Saddlewood Ranch",
    #                 ],
    #                 "Timberline AS II": [
    #                     "Charcoal", "Barkwood", "Hickory", "Pewter Gray",
    #                     "Shakewood", "Slate", "Weathered Wood",
    #                 ],
    #                 "Timberline CS": [
    #                     "Antique Slate", "Barkwood", "Weathered Wood",
    #                 ],
    #                 "Timberline HD": [
    #                     "Barkwood", "Charcoal", "Hunter Green", "Mission Brown", "Hickory",
    #                     "Oyster Gray", "Patriot Red", "Shakewood", "Pewter Gray", "Slate",
    #                     "Sunset Brick", "Weathered Wood", "Birchwood", "White",
    #                     "Williamsburg Slate", "Biscayne Blue", "Canadian Driftwood",
    #                     "Copper Canyon", "Driftwood", "Golden Amber", "Fox Hollow Gray",
    #                 ],
    #                 "Timberline HDZ": [
    #                     "Birchwood", "Barkwood", "Charcoal", "Driftwood", "Hickory",
    #                     "Hunter Green", "Mission Brown", "Oyster Gray", "Pewter Gray",
    #                     "Shakewood", "Slate", "Weathered Wood",
    #                 ],
    #                 "Timberline HDZ RS": [
    #                     "Stone Gray", "Charcoal", "Hickory", "Copper Canyon", "Aged Chestnut",
    #                     "Coastal Slate", "Sagewood", "Birchwood", "Sandalwood", "Golden Amber",
    #                 ],
    #                 "Timberline NS": [
    #                     "Barkwood", "Charcoal", "Arctic White", "Hickory", "Pewter Gray",
    #                     "Shakewood", "Slate", "Hunter Green", "Weathered Wood",
    #                 ],
    #                 "Timberline UHD": [
    #                     "Barkwood", "Birchwood", "Charcoal", "Fox Hollow Gray", "Hickory",
    #                     "Hunter Green", "Pewter Gray", "Patriot Red", "Shakewood", "Slate",
    #                     "Weathered Wood", "Biscayne Blue", "Oyster Gray", "Sunset Brick", "White",
    #                 ],
    #             },
    #
    #             "Designer": {
    #                 "Camelot II": [
    #                     "Barkwood", "Weathered Timber", "Charcoal",
    #                     "Antique Slate", "Royal Slate", "Weathered Wood",
    #                 ],
    #                 "Glenwood": [
    #                     "Weathered Wood", "Golden Prairie", "Autumn Harvest",
    #                     "Dusky Gray", "Adobe Clay", "Chelsea Gray",
    #                 ],
    #                 "Grand Canyon™": [
    #                     "Stonewood", "Black Oak", "Mission Brown",
    #                     "Storm Cloud", "Sedona Sunset",
    #                 ],
    #                 "Grand Sequoia": [
    #                     "Autumn Brown", "Cedar", "Charcoal", "Mesa Brown",
    #                     "Slate", "Weathered Timber", "Weathered Wood",
    #                 ],
    #                 "Grand Sequoia AS": [
    #                     "Adobe Sunset", "Charcoal", "Dusky Gray", "Weathered Wood",
    #                 ],
    #                 "Grand Sequoia RS": [
    #                     "Charcoal", "Forest Brown", "Ocean Gray", "Sagewood", "Sandalwood",
    #                 ],
    #                 "Grand Sequoia RS+": [
    #                     "Charcoal", "Forest Brown",
    #                 ],
    #                 "Slateline": [
    #                     "Antique Slate", "Emerald Green", "English Gray",
    #                     "Royal Slate", "Weathered Slate",
    #                 ],
    #                 "Woodland": [
    #                     "Castlewood Gray", "Cedarwood Abbey", "Tuscan Sunset",
    #                     "Woodberry Brown", "Canterbury Black",
    #                 ],
    #             },
    #
    #             "3-Tab": {
    #                 "Marquis Weathermax": [
    #                     "Autumn Brown", "Charcoal", "Weathered Gray",
    #                 ],
    #                 "Royal Sovereign": [
    #                     "Ash Brown", "Silver Lining", "Slate", "Summer Sage", "White",
    #                     "Weathered Gray", "Autumn Brown", "Charcoal", "Cypress Tan",
    #                     "Golden Cedar", "Nickel Gray", "Russet Red", "Sandrift", "Desert Sand",
    #                 ],
    #             },
    #     }
    # },

    # 5) TRIM
    "Trim": {
        "categories": {  # if your FE expects a different label, adjust this key only
            "Aluminum Trim and Accessories": [
                "Bright White", "Sandstone", "Cashmere", "Almond", "Maize",
                "Monterey Sand", "Cream", "Canyon Clay", "Wicker", "Pebble",
                "Brownstone", "Dover Gray", "Metallic Gray", "Sage",
                "Juniper Grove", "Storm", "Sable", "Windswept Smoke",
                "Midnight Surf", "Wedgewood Blue", "Rockwell Blue",
                "Coastal Blue", "Ivy Green", "Slate", "Dark Drift",
                "Espresso", "Moonlit Moss", "Chestnut Brown",
                "Commercial Brown", "Nutmeg", "Antique Brown",
                "Forest Green", "Graphite", "Iron Ore", "Black",
                "Chesapeake Gray", "Majestic Brick", "Rockport Brown",
                "Smoked Timber", "Meadow Fern", "Marine Dusk", "Hudson Slate",
            ],
            "Vinyl Trim and Accessories": [
                "Almond", "Amber", "Canyon Clay", "Chesapeake Gray",
                "Coastal Blue", "Dark Drift", "Dover Gray", "Espresso",
                "Hudson Slate", "Iron Ore", "Juniper Grove", "Linen", "Maize",
                "Majestic Brick", "Marine Dusk", "Meadow Fern", "Midnight Surf",
                "Monteray Sand", "Moonlit Moss", "Pearl", "Pebble",
                "Rockport Brown", "Rockwell Blue", "Sage", "Sandstone",
                "Smoked Timber", "Snow White", "Storm", "Wicker",
                "Windswept Smoke", "BarnBoard Grey", "Honey Super Matte",
                "Super Matte Modern Walnut", "Sun Bleached Oak",
                "Cinnamon Walnut", "Barrel Oak", "Toffee", "Charred Black",
                "Atlantic White", "Chai Cedar", "Brushed Metallic", "Pure White",
            ],
            "Gentek Performance G8 Piece": [
                "Ice White", "Bright White", "Pebble", "Commercial Brown",
                "Slate", "Iron Ore", "Black",
            ],
        }
    },

    # 6) WINDOW AND DOOR TRIM
    "Window and Door Trim": {
        "categories": {  # if your FE expects a different label, adjust this key only
            "Aluminum Trim and Accessories": [
                "Bright White", "Sandstone", "Cashmere", "Almond", "Maize",
                "Monterey Sand", "Cream", "Canyon Clay", "Wicker", "Pebble",
                "Brownstone", "Dover Gray", "Metallic Gray", "Sage",
                "Juniper Grove", "Storm", "Sable", "Windswept Smoke",
                "Midnight Surf", "Wedgewood Blue", "Rockwell Blue",
                "Coastal Blue", "Ivy Green", "Slate", "Dark Drift",
                "Espresso", "Moonlit Moss", "Chestnut Brown",
                "Commercial Brown", "Nutmeg", "Antique Brown",
                "Forest Green", "Graphite", "Iron Ore", "Black",
                "Chesapeake Gray", "Majestic Brick", "Rockport Brown",
                "Smoked Timber", "Meadow Fern", "Marine Dusk", "Hudson Slate",
            ],
            "Vinyl Trim and Accessories": [
                "Almond", "Amber", "Canyon Clay", "Chesapeake Gray",
                "Coastal Blue", "Dark Drift", "Dover Gray", "Espresso",
                "Hudson Slate", "Iron Ore", "Juniper Grove", "Linen", "Maize",
                "Majestic Brick", "Marine Dusk", "Meadow Fern", "Midnight Surf",
                "Monteray Sand", "Moonlit Moss", "Pearl", "Pebble",
                "Rockport Brown", "Rockwell Blue", "Sage", "Sandstone",
                "Smoked Timber", "Snow White", "Storm", "Wicker",
                "Windswept Smoke", "BarnBoard Grey", "Honey Super Matte",
                "Super Matte Modern Walnut", "Sun Bleached Oak",
                "Cinnamon Walnut", "Barrel Oak", "Toffee", "Charred Black",
                "Atlantic White", "Chai Cedar", "Brushed Metallic", "Pure White",
            ],
            "Gentek Performance G8 Piece": [
                "Ice White", "Bright White", "Pebble", "Commercial Brown",
                "Slate", "Iron Ore", "Black",
            ],
        }
    },

    # 7) WINDOWS
#     "Window": {
#     "categories": {
#         "Regency": {
#             "Regency Awning": {
#                 "Configuration": [
#                     "Single",
#                     "Picture over Awning",
#                     "Double Awning",
#                     "Awning/Picture"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": [
#                     "Colonial",
#                     "Diamond",
#                     "Prairie",
#                     "Double Prairie"
#                 ],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             },
#             "Regency Casement": {
#                 "Configuration": [
#                     "Single Lite - Left Operating",
#                     "Single Lite - Right Operating",
#                     "2 Lite - Left Operating",
#                     "2 Lite - Right Operating",
#                     "3 Lite - L/Picture/R",
#                     "4 Lite",
#                     "4 Lite - L/P/P/R",
#                     "5 Lite"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": [],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             },
#             "Regency Hung": {
#                 "Configuration": [
#                     "1 Lite",
#                     "2 Lite",
#                     "3 Lite",
#                     "4 Lite",
#                     "Hung/Picture/Hung"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": ["No Grilles Selected"],
#                 "Glass": [
#                     "Light Glass",
#                     "Dark Glass",
#                     "Beveled-Leaded St. Joseph",
#                     "Beveled-Leaded Jackson",
#                     "Beveled-Leaded Hanna",
#                     "Beveled-Leaded Vicksburg"
#                 ]
#             },
#             "Regency Picture": {
#                 "Configuration": [
#                     "Single",
#                     "Picture over Awning",
#                     "Double Awning",
#                     "Awning/Picture"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [],
#                 "Grille Style": [],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             },
#             "Regency Slider": {
#                 "Configuration": [
#                     "2 Lite - Left Operating",
#                     "2 Lite - Right Operating",
#                     "Picture over 2 Lite - Left Operating",
#                     "Picture over 2 Lite - Right Operating"
#                 ],
#                 "Exterior Finish": ["Definity Vinyl"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": ["No Grids Selected"],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             }
#         },
#         "Regency 400": {
#             "Regency 400 Awning": {
#                 "Configuration": [
#                     "Single",
#                     "Picture over Awning",
#                     "Double Awning",
#                     "Awning/Picture"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": ["No Grilles Selected"],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             },
#             "Regency 400 Casement": {
#                 "Configuration": [
#                     "Single Lite - Left Operating",
#                     "Single Lite - Right Operating",
#                     "2 Lite - Left Operating",
#                     "2 Lite - Right Operating",
#                     "3 Lite - L/Picture/R",
#                     "4 Lite",
#                     "4 Lite - L/P/P/R",
#                     "5 Lite"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": ["No Grilles Selected"],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             },
#             "Regency 400 Hung": {
#                 "Configuration": [
#                     "1 Lite",
#                     "2 Lite",
#                     "3 Lite",
#                     "4 Lite",
#                     "Hung/Picture/Hung"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": ["No Grilles Selected"],
#                 "Glass": [
#                     "Light Glass",
#                     "Dark Glass",
#                     "Beveled-Leaded St. Joseph",
#                     "Beveled-Leaded Jackson",
#                     "Beveled-Leaded Hanna",
#                     "Beveled-Leaded Vicksburg"
#                 ]
#             },
#             "Regency 400 Picture": {
#                 "Configuration": [
#                     "Single",
#                     "Picture over Awning",
#                     "Double Awning",
#                     "Awning/Picture"
#                 ],
#                 "Exterior Finish": ["Frame Colour"],
#                 "Grille Type": [],
#                 "Grille Style": [],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             },
#             "Regency 400 Slider": {
#                 "Configuration": [
#                     "2 Lite - Left Operating",
#                     "2 Lite - Right Operating",
#                     "Picture over 2 Lite - Left Operating",
#                     "Picture over 2 Lite - Right Operating"
#                 ],
#                 "Exterior Finish": ["Definity Vinyl"],
#                 "Grille Type": [
#                     "No Grilles",
#                     "Flat",
#                     "Euro Contoured",
#                     "Rectangular Pewter",
#                     "Simulated Divided Lites 1 1/4",
#                     "Simulated Divided Lites 2",
#                     "V-Grooved Cut Glass"
#                 ],
#                 "Grille Style": [],
#                 "Glass": [
#                     "Obscure",
#                     "Niagara",
#                     "Glue Chip",
#                     "Satin",
#                     "Bronze Tint",
#                     "Gray Tint"
#                 ]
#             }
#         }
#     }
# },


    # # 8) ENTRY DOOR
    # "Door": {
    #     "categories": {
    #         "Steel Doors": {
    #             "Configuration": [
    #                 "R Door", "S - Door", "Door - S",
    #                 "S - L Door - S", "S - R Door - S",
    #                 "Double Door", "S - Double Door - S", "Side"
    #             ],
    #             "Panel": [
    #                 "Full Glass", "3/4 Glass", "684"
    #             ],
    #             "Glass": [
    #                 "Tilt and Raise Blinds", "Topaz", "Trace",
    #                 "Verdana", "Clear", "Clear Colonial 2x5",
    #                 "Clear Colonial 3x5", "Clear Prairie",
    #                 "Bristol (Satin Nickel Caming)", "Casablanca",
    #                 "Catalina", "Cut Crystal", "Cadence",
    #                 "Cirrus", "Entropy", "Expression (Brass Caming)",
    #                 "Expression (Satin Nickel Caming)", "Greenfield",
    #                 "Heirlooms (Brass Caming)"
    #             ],
    #             "Handles": [
    #                 "Amherst Satin Chrome",
    #                 "Ashfield Venetian Bronze"
    #             ]
    #         }
    #     }
    # },
}
