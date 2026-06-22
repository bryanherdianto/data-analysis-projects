SELECT
  app_id,
  ROUND(100.0 * COUNT(CASE WHEN event_type = 'click' THEN 1 ELSE NULL END) /
  COUNT(CASE WHEN event_type = 'impression' THEN 1 ELSE NULL END), 2) AS ctr
FROM events
WHERE EXTRACT(YEAR FROM timestamp) = 2022
GROUP BY app_id;
