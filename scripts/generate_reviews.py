import pandas as pd
import random

orders_df = pd.read_csv("data/orders.csv")

reviews = []

review_templates = {

    5: [
        "Amazing product",
        "Highly recommended",
        "Worth every penny",
        "Excellent quality",
        "Very satisfied"
    ],

    4: [
        "Good quality",
        "Satisfied with purchase",
        "Works as expected",
        "Nice product"
    ],

    3: [
        "Average product",
        "Okay for the price",
        "Nothing special",
        "Could be better"
    ],

    2: [
        "Delivery was late",
        "Expected better quality",
        "Not fully satisfied"
    ],

    1: [
        "Very disappointed",
        "Poor quality",
        "Not worth the money",
        "Terrible experience"
    ]
}

for review_num in range(1, 8001):

    order = orders_df.sample(1).iloc[0]

    rating = random.choices(
        [1,2,3,4,5],
        weights=[10,10,20,25,35]
    )[0]

    review_text = random.choice(
        review_templates[rating]
    )

    if rating >= 4:
        sentiment = "Positive"
    elif rating == 3:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"

    reviews.append({
        "review_id": f"R{review_num:05d}",
        "customer_id": order["customer_id"],
        "product_id": order["product_id"],
        "rating": rating,
        "review_text": review_text,
        "sentiment_label": sentiment,
        "review_date": order["order_date"]
    })

reviews_df = pd.DataFrame(reviews)

reviews_df.to_csv(
    "data/reviews.csv",
    index=False
)

print("\nSample Reviews\n")
print(reviews_df.head(10).to_string(index=False))
print()
print(f"Total Reviews: {len(reviews_df)}")