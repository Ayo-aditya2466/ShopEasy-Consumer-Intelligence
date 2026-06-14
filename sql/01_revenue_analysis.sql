-- Funnel Events

SELECT event_type,
       COUNT(*) AS users
FROM funnel_events
GROUP BY event_type
ORDER BY users DESC;

-- Traffic Source Analysis

SELECT traffic_source,
       COUNT(*) AS users
FROM funnel_events
GROUP BY traffic_source
ORDER BY users D

SELECT device_type,
       COUNT(*) AS users
FROM funnel_events
GROUP BY device_type
ORDER BY users DESC;