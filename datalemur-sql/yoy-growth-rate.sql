WITH user_transactions_cte AS (
  SELECT
    EXTRACT(YEAR FROM transaction_date) AS yr,
    product_id,
    SUM(spend) AS curr_year_spend,
    LAG(SUM(spend), 1) OVER(
      PARTITION BY product_id
      ORDER BY EXTRACT(YEAR FROM transaction_date)
    ) AS prev_year_spend
  FROM user_transactions
  GROUP BY EXTRACT(YEAR FROM transaction_date), product_id
)
SELECT
  yr,
  product_id,
  curr_year_spend,
  prev_year_spend,
  ROUND(
    100 * (curr_year_spend - prev_year_spend) / prev_year_spend::NUMERIC,
  2) AS yoy_rate
FROM user_transactions_cte;
