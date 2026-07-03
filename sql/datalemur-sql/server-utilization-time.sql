WITH cte_server_utilization AS (
  SELECT
    server_id,
    session_status,
    status_time AS start_time,
    LEAD(status_time, 1) OVER (
      PARTITION BY server_id
      ORDER BY status_time) AS stop_time
  FROM server_utilization
)
SELECT
  DATE_PART('days', JUSTIFY_HOURS(SUM(stop_time - start_time))) AS total_uptime_days
FROM cte_server_utilization
WHERE session_status = 'start'
  AND stop_time IS NOT NULL;
