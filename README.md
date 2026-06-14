# ShopEasy Consumer Intelligence Dashboard

An end-to-end retail analytics project built to analyze sales performance, customer behavior, product trends, review sentiment, and business opportunities for **ShopEasy**.

This project combines **SQL**, **Python**, **PostgreSQL**, **Power BI**, and **business storytelling** to transform raw data into actionable insights.

---

## Project Overview

ShopEasy is an e-commerce business with data spread across:
- Customers
- Products
- Orders
- Reviews
- Funnel Events

The goal of this project is to understand:
- What drives revenue
- Who the customers are
- Which products perform best
- What customers feel about the products
- Where business growth opportunities exist

---

## Business Questions Answered

- Which category generates the most revenue?
- Which brands and products are the top performers?
- Are new customers or returning customers more valuable?
- Which cities contribute the most revenue?
- What do customers think about the products?
- Which products receive the most positive and negative feedback?
- How does revenue trend over time?

---

## Tools Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **PostgreSQL**
- **SQL**
- **Power BI**
- **Colab / Jupyter Notebook**

---

## Project Workflow

### Phase 0: Environment Setup
Configured the development environment and required tools.

### Phase 1: Business Understanding
Defined the business problem and the key questions to be answered.

### Phase 2: Data Generation
Created synthetic datasets for:
- `customers.csv`
- `products.csv`
- `orders.csv`
- `reviews.csv`
- `funnel_events.csv`

### Phase 3: PostgreSQL Database
Loaded the datasets into PostgreSQL and structured them into relational tables.

### Phase 4: SQL Analytics
Performed business analysis using SQL across:
- Revenue
- Customers
- Products
- Reviews
- Funnel events

### Phase 5: Python EDA
Performed exploratory analysis, data quality checks, cleaning, and visual analysis in Python.

### Phase 6: Sentiment Analysis
Analyzed review text and sentiment labels to understand customer opinion.

### Phase 7: Power BI Dashboard
Built an interactive 3-page dashboard:
- Executive Dashboard
- Customer Analytics
- Product Performance

### Phase 8: Business Recommendations
Converted findings into business recommendations.

### Phase 9: GitHub Portfolio Packaging
Prepared the project for portfolio presentation and sharing.

---

## Datasets

### 1. Customers
Contains:
- `customer_id`
- `customer_name`
- `gender`
- `age`
- `city`
- `join_date`
- `customer_type`

### 2. Products
Contains:
- `product_id`
- `product_name`
- `brand`
- `category`
- `base_price`

### 3. Orders
Contains:
- `order_id`
- `customer_id`
- `product_id`
- `quantity`
- `discount_pct`
- `final_amount`
- `payment_method`
- `order_date`

### 4. Reviews
Contains:
- `review_id`
- `customer_id`
- `product_id`
- `rating`
- `review_text`
- `sentiment_label`
- `review_date`

### 5. Funnel Events
Contains:
- `event_id`
- `customer_id`
- `event_type`
- `event_date`
- `device_type`
- `traffic_source`

---

## Key Insights

- Electronics contributes nearly **89%** of total revenue.
- Apple and Sony are the highest revenue-generating brands.
- New customers contribute more revenue than returning customers.
- Mumbai is the top revenue-generating city.
- Customers aged **55+** contribute the highest revenue.
- Positive reviews account for the majority of customer feedback.
- AirPods Pro is one of the top revenue-generating products.

---

## Power BI Dashboard Pages

### 1. Executive Dashboard
Focuses on company-wide performance:
- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Revenue Trend
- Revenue by Category
- Top Brands
- Payment Method Distribution

### 2. Customer Analytics
Focuses on customer segments and revenue contribution:
- Customer Type Distribution
- Revenue by Customer Type
- Customers by City
- Revenue by Age Group
- Revenue by City

### 3. Product Performance
Focuses on product-level performance and customer feedback:
- Top 10 Products by Revenue
- Rating Distribution
- Sentiment Distribution
- Revenue Share by Category
- Key Insights

---

## SQL Analysis Files

The SQL folder contains the final business queries used for analysis:

- `01_revenue_analysis.sql`
- `02_customer_analysis.sql`
- `03_product_analysis.sql`
- `04_review_analysis.sql`
- `05_funnel_analysis.sql`

---

## Folder Structure

```text
ShopEasy-Consumer-Intelligence/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── reviews.csv
│   └── funnel_events.csv
│
├── images/
│   ├── executive_dashboard.png
│   ├── customer_analytics.png
│   └── product_performance.png
│
├── notebook/
│   └── ShopEasy_EDA.ipynb
│
├── powerbi/
│   └── ShopEasy_Dashboard.pbix
│
├── scripts/
│   ├── generate_customers.py
│   ├── generate_products.py
│   ├── generate_orders.py
│   ├── generate_reviews.py
│   └── generate_funnel_events.py
│
├── sql/
│   ├── 01_revenue_analysis.sql
│   ├── 02_customer_analysis.sql
│   ├── 03_product_analysis.sql
│   ├── 04_review_analysis.sql
│   └── 05_funnel_analysis.sql
│
└── README.md