import pandas as pd
import random

# ==========================
# PRODUCT CATALOG
# ==========================

products_catalog = {

    "Electronics": {

        "Apple": {
            "products": [
                "iPhone 15",
                "iPhone 15 Plus",
                "iPhone 15 Pro",
                "MacBook Air",
                "AirPods Pro",
                "Apple Watch Series 9"
            ],
            "price_range": (15000, 120000)
        },

        "Samsung": {
            "products": [
                "Galaxy S24",
                "Galaxy S24 Ultra",
                "Galaxy Buds 3",
                "Galaxy Watch 6",
                "Samsung Smart TV"
            ],
            "price_range": (8000, 90000)
        },

        "Sony": {
            "products": [
                "WH-1000XM5",
                "Bravia TV",
                "Xperia Smartphone",
                "Sony Soundbar"
            ],
            "price_range": (5000, 100000)
        },

        "JBL": {
            "products": [
                "Flip Speaker",
                "Charge Speaker",
                "Wave Beam Earbuds",
                "JBL PartyBox"
            ],
            "price_range": (2000, 30000)
        },

        "Boat": {
            "products": [
                "Airdopes 141",
                "Stone Speaker",
                "Boat Smart Ring",
                "Boat Wave Watch"
            ],
            "price_range": (1000, 10000)
        }
    },

    "Fashion": {

        "Nike": {
            "products": [
                "Air Max Shoes",
                "Sports Hoodie",
                "Running Shorts",
                "Training T-Shirt"
            ],
            "price_range": (1000, 12000)
        },

        "Adidas": {
            "products": [
                "Ultraboost Shoes",
                "Track Jacket",
                "Training Tee",
                "Sports Pants"
            ],
            "price_range": (1000, 12000)
        },

        "Puma": {
            "products": [
                "Running Shoes",
                "Gym T-Shirt",
                "Sports Jacket",
                "Track Pants"
            ],
            "price_range": (800, 10000)
        },

        "Levis": {
            "products": [
                "511 Jeans",
                "Denim Jacket",
                "Casual Shirt",
                "Slim Fit Jeans"
            ],
            "price_range": (1000, 8000)
        },

        "H&M": {
            "products": [
                "Oversized T-Shirt",
                "Cargo Pants",
                "Basic Hoodie",
                "Casual Sweatshirt"
            ],
            "price_range": (500, 6000)
        }
    }
}

# ==========================
# GENERATE PRODUCTS
# ==========================

products = []

product_id = 1

for category, brands in products_catalog.items():

    for brand, details in brands.items():

        min_price, max_price = details["price_range"]

        for product_name in details["products"]:

            base_price = round(
                random.uniform(min_price, max_price),
                2
            )

            products.append({
                "product_id": f"P{product_id:04d}",
                "product_name": product_name,
                "brand": brand,
                "category": category,
                "base_price": base_price
            })

            product_id += 1

# ==========================
# CREATE DATAFRAME
# ==========================

products_df = pd.DataFrame(products)

# ==========================
# EXPORT CSV
# ==========================

products_df.to_csv(
    "data/products.csv",
    index=False
)

print("products.csv created successfully!")
print(products_df.head(15))