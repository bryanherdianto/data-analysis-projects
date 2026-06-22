SELECT 
  DISTINCT user_id
FROM emails as e
INNER JOIN texts as t
  ON e.email_id = t.email_id
WHERE t.action_date = e.signup_date + INTERVAL '1 day'
  AND t.signup_action = 'Confirmed';
