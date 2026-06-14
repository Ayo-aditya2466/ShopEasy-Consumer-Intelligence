import pandas as pd
import random
from faker import Faker

fake = Faker()

products_df = pd.read_csv("data/products.csv")
customers_df = pd.read_csv("data/customers.csv")

orders = []

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

discounts = [0, 5, 10, 15, 20]

for order_num in range(1, 20001):

    customer = customers_df.sample(1).iloc[0]
    product = products_df.sample(1).iloc[0]

    quantity = random.randint(1, 5)

    discount_pct = random.choice(discounts)

    final_amount = round(
        product["base_price"]
        * quantity
        * (1 - discount_pct / 100),
        2
    )

    orders.append({
        "order_id": f"O{order_num:05d}",
        "customer_id": customer["customer_id"],
        "product_id": product["product_id"],
        "quantity": quantity,
        "discount_pct": discount_pct,
        "final_amount": final_amount,
        "payment_method": random.choice(payment_methods),
        "order_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/orders.csv",
    index=False
)

print(orders_df.head(10))
print()
print(f"Total Orders: {len(orders_df)}")
pd.read_csv("data/orders.csv")