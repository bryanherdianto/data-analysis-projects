SELECT
  COALESCE(advertiser.user_id, daily_pay.user_id) AS user_id,
  CASE
    WHEN advertiser.user_id IN (SELECT user_id FROM daily_pay) AND advertiser.status IN ('NEW', 'EXISTING', 'RESURRECT')
      THEN 'EXISTING'
    WHEN advertiser.user_id IN (SELECT user_id FROM daily_pay) AND advertiser.status = 'CHURN'
      THEN 'RESURRECT'
    WHEN advertiser.user_id IS NULL
      THEN 'NEW'
    WHEN advertiser.user_id NOT IN (SELECT user_id FROM daily_pay)
      THEN 'CHURN'
  END AS new_status
FROM advertiser
FULL OUTER JOIN daily_pay
  ON advertiser.user_id = daily_pay.user_id
ORDER BY user_id;
