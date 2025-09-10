{{ config(materialized = 'table') }}

select *,
    -- Calculate ride duration in minutes
    date_diff('minute', started_at, ended_at) as ride_duration_minutes,
    -- Extract time dimensions
    extract(
        hour
        from started_at
    ) as start_hour,
    extract(
        dayofweek
        from started_at
    ) as start_day_of_week,
    extract(
        month
        from started_at
    ) as start_month,
    date_trunc('day', started_at) as ride_date,
    -- Classify ride types
    case
        when date_diff('minute', started_at, ended_at) <= 10 then 'short'
        when date_diff('minute', started_at, ended_at) <= 30 then 'medium'
        else 'long'
    end as ride_duration_category,
    -- Simple NYC approximation (latitude ~40.7°)
    111.32 * sqrt(
        pow(end_latitude - start_latitude, 2) + pow((end_longitude - start_longitude) * 0.74, 2)
    ) as distance_km,
    -- Add data quality flags
    case
        when started_at >= ended_at then 'invalid_duration'
        when date_diff('minute', started_at, ended_at) > 1440 then 'too_long'
        when date_diff('minute', started_at, ended_at) < 1 then 'too_short'
        else 'valid'
    end as duration_quality_flag
from {{ ref('stg_rides') }}
where started_at < ended_at