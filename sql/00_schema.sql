-- =====================================================
-- ShopEasy Consumer Intelligence Dashboard
-- Database Schema
-- =====================================================


-- =====================================================
-- Customers Table
-- =====================================================

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    gender VARCHAR(20),
    age INTEGER,
    city VARCHAR(100),
    join_date DATE,
    customer_type VARCHAR(50)
);

-- =====================================================
-- Products Table
-- =====================================================

CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(150),
    brand VARCHAR(100),
    category VARCHAR(100),
    base_price NUMERIC(10,2)
);

-- =====================================================
-- Orders Table
-- =====================================================

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    quantity INTEGER,
    discount_pct NUMERIC(5,2),
    final_amount NUMERIC(12,2),
    payment_method VARCHAR(50),
    order_date DATE,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_orders_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

-- =====================================================
-- Reviews Table
-- =====================================================

CREATE TABLE reviews (
    review_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    rating INTEGER,
    review_text TEXT,
    sentiment_label VARCHAR(20),
    review_date DATE,

    CONSTRAINT fk_reviews_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_reviews_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

-- =====================================================
-- Funnel Events Table
-- =====================================================

CREATE TABLE funnel_events (
    event_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    event_type VARCHAR(50),
    event_date DATE,
    device_type VARCHAR(50),
    traffic_source VARCHAR(100),

    CONSTRAINT fk_funnel_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);