WITH measurement_row AS (
  SELECT
    measurement_time::DATE AS measurement_day,
    measurement_value,
    ROW_NUMBER() OVER(PARTITION BY measurement_time::DATE ORDER BY measurement_time)
  FROM measurements
)
SELECT
  measurement_day,
  SUM(CASE WHEN MOD(row_number, 2) <> 0 THEN measurement_value 
           ELSE NULL END) AS odd_sum,
  SUM(CASE WHEN MOD(row_number, 2) = 0 THEN measurement_value 
           ELSE NULL END) AS even_sum
FROM measurement_row
GROUP BY measurement_day;
