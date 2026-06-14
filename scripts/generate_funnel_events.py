import pandas as pd
import random
from faker import Faker

fake = Faker()

customers_df = pd.read_csv("data/customers.csv")

events = []

event_types = [
    "Visit",
    "Product View",
    "Add To Cart",
    "Checkout",
    "Purchase"
]

event_weights = [
    40,
    25,
    15,
    10,
    10
]

device_types = [
    "Mobile",
    "Desktop",
    "Tablet"
]

traffic_sources = [
    "Google",
    "Facebook",
    "Instagram",
    "Direct"
]

for event_num in range(1, 50001):

    customer = customers_df.sample(1).iloc[0]

    event_type = random.choices(
        event_types,
        weights=event_weights
    )[0]

    events.append({
        "event_id": f"E{event_num:05d}",
        "customer_id": customer["customer_id"],
        "event_type": event_type,
        "event_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "device_type": random.choice(device_types),
        "traffic_source": random.choice(traffic_sources)
    })

events_df = pd.DataFrame(events)

events_df.to_csv(
    "data/funnel_events.csv",
    index=False
)

print(events_df.head(10).to_string(index=False))
print()
print(f"Total Events: {len(events_df)}")