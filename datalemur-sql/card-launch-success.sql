WITH cte_monthly_cards_issued AS (
  SELECT
    card_name,
    issued_amount,
    RANK() OVER(PARTITION BY card_name ORDER BY issue_year, issue_month)
  FROM monthly_cards_issued
)
SELECT
  card_name,
  issued_amount
FROM cte_monthly_cards_issued
WHERE rank = 1
ORDER BY issued_amount DESC;
