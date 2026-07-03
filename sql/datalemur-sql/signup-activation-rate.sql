SELECT
  ROUND(
    COUNT(CASE WHEN signup_action = 'Confirmed' THEN 1 
               ELSE NULL END)::NUMERIC /
    COUNT(CASE WHEN signup_action = 'Confirmed' THEN 1
               WHEN signup_action = 'Not Confirmed' THEN 1
               ELSE NULL END),
  2) AS activation_rate
FROM emails AS e
INNER JOIN texts AS t
  ON e.email_id = t.email_id;
