SELECT 
  manufacturer,
  '$' || ROUND(SUM(total_sales)::NUMERIC / 1000000, 0) || ' million' AS sales_mil
FROM pharmacy_sales
GROUP BY manufacturer
ORDER BY 
  ROUND(SUM(total_sales)::NUMERIC / 1000000, 0) DESC, 
  manufacturer DESC;
