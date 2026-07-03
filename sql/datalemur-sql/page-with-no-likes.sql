SELECT 
  p.page_id
FROM pages AS p
LEFT JOIN page_likes AS l
ON p.page_id = l.page_id
WHERE l.page_id IS NULL
ORDER BY p.page_id
