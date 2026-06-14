-- Rating Distribution

SELECT rating,
       COUNT(*) AS total_reviews
FROM reviews
GROUP BY rating
ORDER BY rating;

-- Sentiment Distribution

SELECT sentiment_label,
       COUNT(*) AS total_reviews
FROM reviews
GROUP BY sentiment_label
ORDER BY total_reviews DESC;

-- Average Product Rating

SELECT ROUND(AVG(rating),2) AS average_rating
FROM reviews;