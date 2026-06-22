SELECT
  ROUND(
    100 * COUNT(CASE WHEN caller.country_id <> receiver.country_id THEN 1 
                     ELSE NULL END) /
    COUNT(calls.caller_id)::NUMERIC, 
  1) AS international_calls_pct
FROM phone_calls AS calls
LEFT JOIN phone_info AS caller
  ON calls.caller_id = caller.caller_id
LEFT JOIN phone_info AS receiver
  ON calls.receiver_id = receiver.caller_id;
