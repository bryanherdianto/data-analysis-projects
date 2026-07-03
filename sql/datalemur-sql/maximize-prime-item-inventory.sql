WITH summary AS (
  SELECT
    item_type,
    COUNT(*) AS item_count,
    SUM(square_footage) AS item_type_square_footage
  FROM inventory
  GROUP BY item_type
)
SELECT
  item_type,
  CASE
    WHEN item_type = 'prime_eligible' 
      THEN item_count * FLOOR(500000 / item_type_square_footage)
    WHEN item_type = 'not_prime' 
      THEN item_count * FLOOR((SELECT MOD(500000, SUM(square_footage)) 
                               FROM inventory 
                               WHERE item_type = 'prime_eligible' 
                               GROUP BY item_type) / item_type_square_footage)
  END AS item_count
FROM summary
ORDER BY item_count DESC;
