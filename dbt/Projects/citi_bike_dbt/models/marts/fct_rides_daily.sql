{{ config(materialized = 'table') }}

select ride_date,
    count(*) as total_rides,
    count(
        case
            when member_type = 'member' then 1
        end
    ) as member_rides,
    count(
        case
            when member_type = 'casual' then 1
        end
    ) as casual_rides,
    round(avg(ride_duration_minutes), 2) as avg_duration_minutes,
    count(
        case
            when ride_duration_category = 'short' then 1
        end
    ) as short_rides,
    count(
        case
            when ride_duration_category = 'medium' then 1
        end
    ) as medium_rides,
    count(
        case
            when ride_duration_category = 'long' then 1
        end
    ) as long_rides,
    count(distinct start_station_id) as unique_start_stations,
    count(distinct end_station_id) as unique_end_stations
from {{ ref('int_rides_with_duration') }}
group by ride_date
order by ride_date