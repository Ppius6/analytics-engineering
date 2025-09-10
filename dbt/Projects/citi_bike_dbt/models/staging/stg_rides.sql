{{ config(materialized = 'view') }}

select ride_id,
    rideable_type,
    start_station_name,
    start_station_id,
    end_station_name,
    end_station_id,
    member_casual as member_type,
    cast(regexp_replace(started_at, ' \+\d{4}$', '') as timestamp) as started_at,
    cast(regexp_replace(ended_at, ' \+\d{4}$', '') as timestamp) as ended_at,
    cast(start_lat as double) as start_latitude,
    cast(start_lng as double) as start_longitude,
    cast(end_lat as double) as end_latitude,
    cast(end_lng as double) as end_longitude
from {{ ref('trips_2024') }}