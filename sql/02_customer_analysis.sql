-- Revenue by Customer Type

SELECT c.customer_type,
       ROUND(SUM(o.final_amount),2) AS revenue
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.customer_type
ORDER BY revenue DESC;

-- Customer Count by City

SELECT city,
       COUNT(*) AS customers
FROM customers
GROUP BY city
ORDER BY customers DESC;

-- Customer Count by Gender

SELECT gender,
       COUNT(*) AS total_customers
FROM customers
GROUP BY gender;