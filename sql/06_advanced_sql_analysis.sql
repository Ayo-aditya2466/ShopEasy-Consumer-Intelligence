-- ============================================================
-- ShopEasy Advanced SQL Analytics
-- Techniques: CTEs, Window Functions, CASE, Subqueries
-- ============================================================


-- -----------------------------------------------
-- 1. Month-over-Month Revenue Growth (LAG)
-- -----------------------------------------------
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', order_date)::date AS month,
        SUM(revenue) AS total_revenue
    FROM orders
    GROUP BY 1
)
SELECT
    month,
    total_revenue,
    LAG(total_revenue) OVER (ORDER BY month) AS prev_month_revenue,
    ROUND(
        (total_revenue - LAG(total_revenue) OVER (ORDER BY month))
        / LAG(total_revenue) OVER (ORDER BY month) * 100, 2
    ) AS mom_growth_pct
FROM monthly_revenue
ORDER BY month;


-- -----------------------------------------------
-- 2. Customer Purchase Frequency Segmentation (CASE + CTE)
-- -----------------------------------------------
WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(order_id) AS total_orders,
        SUM(revenue)    AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT
    CASE
        WHEN total_orders = 1 THEN '1 - One-time Buyer'
        WHEN total_orders BETWEEN 2 AND 3 THEN '2 - Occasional Buyer'
        WHEN total_orders BETWEEN 4 AND 6 THEN '3 - Regular Buyer'
        ELSE '4 - Loyal Buyer'
    END AS customer_segment,
    COUNT(*)                    AS customer_count,
    ROUND(AVG(total_spent), 2)  AS avg_lifetime_value,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2
    ) AS pct_of_customers
FROM customer_orders
GROUP BY 1
ORDER BY 1;


-- -----------------------------------------------
-- 3. Top 3 Products Per Category (RANK)
-- -----------------------------------------------
WITH product_revenue AS (
    SELECT
        p.category,
        p.name AS product_name,
        SUM(o.revenue) AS total_revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY 1, 2
),
ranked AS (
    SELECT
        category,
        product_name,
        total_revenue,
        RANK() OVER (PARTITION BY category ORDER BY total_revenue DESC) AS rank
    FROM product_revenue
)
SELECT category, rank, product_name, total_revenue
FROM ranked
WHERE rank <= 3
ORDER BY category, rank;


-- -----------------------------------------------
-- 4. Customer Retention — First vs Repeat Buyers (CTE + CASE)
-- -----------------------------------------------
WITH first_order AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM orders
    GROUP BY customer_id
),
order_type AS (
    SELECT
        o.order_id,
        o.customer_id,
        o.order_date,
        o.revenue,
        CASE
            WHEN o.order_date = f.first_order_date THEN 'First Purchase'
            ELSE 'Repeat Purchase'
        END AS purchase_type
    FROM orders o
    JOIN first_order f ON o.customer_id = f.customer_id
)
SELECT
    purchase_type,
    COUNT(order_id)        AS total_orders,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(AVG(revenue), 2) AS avg_order_value
FROM order_type
GROUP BY 1;


-- -----------------------------------------------
-- 5. Running Total Revenue by Month (SUM OVER)
-- -----------------------------------------------
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date)::date AS month,
        SUM(revenue) AS monthly_revenue
    FROM orders
    GROUP BY 1
)
SELECT
    month,
    monthly_revenue,
    SUM(monthly_revenue) OVER (ORDER BY month) AS running_total,
    ROUND(
        SUM(monthly_revenue) OVER (ORDER BY month)
        / SUM(monthly_revenue) OVER () * 100, 2
    ) AS cumulative_pct
FROM monthly
ORDER BY month;


-- -----------------------------------------------
-- 6. City-Level Revenue with Percentile Ranking (NTILE)
-- -----------------------------------------------
WITH city_revenue AS (
    SELECT
        c.city,
        COUNT(DISTINCT o.customer_id) AS unique_customers,
        COUNT(o.order_id)             AS total_orders,
        ROUND(SUM(o.revenue), 2)      AS total_revenue
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.city
)
SELECT
    city,
    unique_customers,
    total_orders,
    total_revenue,
    NTILE(4) OVER (ORDER BY total_revenue DESC) AS revenue_quartile
FROM city_revenue
ORDER BY total_revenue DESC;