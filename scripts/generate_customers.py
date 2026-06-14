import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")

customers = []

cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Pune",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Ahmedabad"
]

for customer_id in range(1, 5001):

    customers.append({
        "customer_id": f"C{customer_id:05d}",
        "customer_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 65),
        "city": random.choice(cities),
        "join_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "customer_type": random.choices(
            ["New", "Returning"],
            weights=[70, 30]
        )[0]
    })

customers_df = pd.DataFrame(customers)

# Missing cities (2%)
missing_city_rows = customers_df.sample(
    frac=0.02,
    random_state=42
).index

customers_df.loc[missing_city_rows, "city"] = None

# Missing ages (1%)
missing_age_rows = customers_df.sample(
    frac=0.01,
    random_state=99
).index

customers_df.loc[missing_age_rows, "age"] = None

# City inconsistencies
customers_df.loc[
    customers_df.sample(frac=0.02, random_state=21).index,
    "city"
] = "mumbai"

customers_df.loc[
    customers_df.sample(frac=0.02, random_state=55).index,
    "city"
] = "MUMBAI"



customers_df.to_csv(
    "data/customers.csv",
    index=False
)

print(customers_df.head())
print()
print(f"Total Customers: {len(customers_df)}")
#
# =====================================
# INTRODUCE DATA QUALITY ISSUES
# =====================================

# 2% missing city values
missing_city_rows = customers_df.sample(
    frac=0.02,
    random_state=42
).index

customers_df.loc[
    missing_city_rows,
    "city"
] = None

# 1% missing age values
missing_age_rows = customers_df.sample(
    frac=0.01,
    random_state=99
).index

customers_df.loc[
    missing_age_rows,
    "age"
] = None

# City name inconsistencies
customers_df.loc[
    customers_df.sample(
        frac=0.02,
        random_state=21
    ).index,
    "city"
] = "mumbai"

customers_df.loc[
    customers_df.sample(
        frac=0.02,
        random_state=55
    ).index,
    "city"
] = "MUMBAI"

# Duplicate records (1%)
#duplicates = customers_df.sample(
 #   frac=0.01,
   # random_state=101)

#customers_df = pd.concat(
#   [customers_df, duplicates],
#    ignore_index=True
#)