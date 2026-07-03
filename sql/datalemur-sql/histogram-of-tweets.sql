SELECT 
  f.tweet_bucket, 
  COUNT(*) AS users_num
FROM
(
  SELECT 
    user_id, 
    COUNT(*) AS tweet_bucket
  FROM tweets
  WHERE EXTRACT(YEAR FROM tweet_date) = 2022
  GROUP BY user_id
) AS f
GROUP BY f.tweet_bucket
