WITH cte_transaction_date AS (
  SELECT
    transaction_date,
    user_id,
    DENSE_RANK() OVER(PARTITION BY user_id ORDER BY transaction_date DESC) AS rank
  FROM user_transactions
)
SELECT
  transaction_date,
  user_id,
  COUNT(*) AS purchase_count
FROM cte_transaction_date
WHERE rank = 1
GROUP BY transaction_date, user_id;
