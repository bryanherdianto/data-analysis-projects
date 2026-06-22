WITH cte_items_per_order AS (
  SELECT
    item_count,
    order_occurrences,
    DENSE_RANK() OVER(ORDER BY order_occurrences DESC)
  FROM items_per_order
)
SELECT
  item_count
FROM cte_items_per_order
WHERE dense_rank = 1
ORDER BY item_count;
