WITH top_10 AS (
  SELECT
    artist_name,
    DENSE_RANK() OVER(ORDER BY COUNT(*) DESC) AS artist_rank
  FROM artists AS a
  INNER JOIN songs AS s
    ON a.artist_id = s.artist_id
  INNER JOIN global_song_rank AS g
    ON s.song_id = g.song_id
  WHERE rank <= 10
  GROUP BY artist_name
)
SELECT
  artist_name,
  artist_rank
FROM top_10
WHERE artist_rank <= 5
