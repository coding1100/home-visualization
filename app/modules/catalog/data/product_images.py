# app/modules/catalog/data/product_images.py
# Optional sidecar mapping: absolute path -> image URL.
# Fill as you get assets. Safe to leave empty; API will return null for image_url.

PRODUCT_IMAGE_MAP: dict[str, str] = {
    # examples (you can delete these or expand):
    # "Wall/categories/Brick": "https://cdn.example.com/brick-group.png",
    # "Wall/categories/Brick/Red": "https://cdn.example.com/brick-red.jpg",
    # "Roofing/categories/GAF": "https://cdn.example.com/gaf.jpg",
}