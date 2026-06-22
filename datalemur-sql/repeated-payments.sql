WITH cte_transactions AS (
  SELECT
    merchant_id,
    credit_card_id,
    transaction_timestamp AS curr_transaction_timestamp,
    LEAD(transaction_timestamp, 1) OVER(
      PARTITION BY merchant_id, credit_card_id
      ORDER BY transaction_id
    ) AS next_transaction_timestamp
  FROM transactions
)
SELECT
  COUNT(DISTINCT CONCAT(merchant_id, credit_card_id)) AS payment_count
FROM cte_transactions
WHERE next_transaction_timestamp - curr_transaction_timestamp <= INTERVAL '10 minutes';
