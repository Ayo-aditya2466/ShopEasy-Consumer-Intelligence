-- Top Products by Revenue

SELECT p.product_name,
       ROUND(SUM(o.final_amount),2) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- Revenue by Brand

SELECT p.brand,
       ROUND(SUM(o.final_amount),2) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.brand
ORDER BY revenue DESC;

-- Most Ordered Products

SELECT product_id,
       COUNT(*) AS total_orders
FROM orders
GROUP BY product_id
ORDER BY total_orders DESC;