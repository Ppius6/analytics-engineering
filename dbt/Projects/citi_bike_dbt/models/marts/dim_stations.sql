{{ config(materialized = 'table') }}

with start_stations as (
    select distinct start_station_id as station_id,
        start_station_name as station_name,
        start_latitude as latitude,
        start_longitude as longitude
    from {{ ref('stg_rides') }}
    where start_station_id is not null
),
end_stations as (
    select distinct end_station_id as station_id,
        end_station_name as station_name,
        end_latitude as latitude,
        end_longitude as longitude
    from {{ ref('stg_rides') }}
    where end_station_id is not null
),
all_stations as (
    select *
    from start_stations
    union
    select *
    from end_stations
)
select station_id,
    station_name,
    round(latitude, 6) as latitude,
    round(longitude, 6) as longitude
from all_stations