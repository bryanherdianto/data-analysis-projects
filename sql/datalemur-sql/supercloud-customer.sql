SELECT
  customer_id
FROM customer_contracts AS c
INNER JOIN products AS p
  ON c.product_id = p.product_id
GROUP BY customer_id
HAVING COUNT(DISTINCT product_category) = 3
