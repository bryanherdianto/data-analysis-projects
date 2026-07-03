SELECT
  age_bucket,
  ROUND(
    SUM(CASE WHEN activity_type = 'send' THEN time_spent 
             ELSE NULL END) /
    SUM(CASE WHEN activity_type = 'send' THEN time_spent 
             WHEN activity_type = 'open' THEN time_spent
             ELSE NULL END)::NUMERIC * 100,
  2) AS send_perc,
  ROUND(
    SUM(CASE WHEN activity_type = 'open' THEN time_spent 
             ELSE NULL END) /
    SUM(CASE WHEN activity_type = 'send' THEN time_spent 
             WHEN activity_type = 'open' THEN time_spent
             ELSE NULL END)::NUMERIC * 100,
  2) AS open_perc
FROM activities AS a
INNER JOIN age_breakdown AS ab
  ON a.user_id = ab.user_id
GROUP BY age_bucket
