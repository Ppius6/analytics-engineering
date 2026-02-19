# Working with Dates and Times

## Dates and Calendars

Python has a built-in `datetime` module that provides classes for working with dates and times. The `datetime` class represents a single point in time, while the `date` and `time` classes represent just the date or time components, respectively.

To create a date object, you can use the `date` class:

```python
from datetime import date
my_date = date(2024, 6, 1)
print(my_date)  # Output: 2024-06-01
```

We can access individual components of the date:

```python
from datetime import date
my_date = date(2024, 6, 1)
print(my_date.year)  # Output: 2024
print(my_date.month) # Output: 6
print(my_date.day)   # Output: 1
```

Note: Python counts weekdays from Monday (0) to Sunday (6). You can get the weekday of a date using the `weekday()` method:

```python
from datetime import date
my_date = date(2024, 6, 1)
print(my_date.weekday())  # Output: 5 (Saturday)
```

We can also perform date arithmetics, 

```python

from datetime import date
d1 = date(2024, 6, 1)
d2 = date(2024, 6, 15)
l = [d1, d2]
print(min(l))  # Output: 2024-06-01
print(max(l))  # Output: 2024-06-15
delta = d2 - d1
print(delta)  # Output: 14 days, 0:00:00
print(delta.days)  # Output: 14

```

Apart from just extracting `delta.days`, we can also extract other items such as `delta.seconds` and `delta.microseconds` to get the total duration in seconds or microseconds, respectively. And also perform custom arithmetics such as `weeks = delta.days // 7` to get the number of weeks in the duration or `remaining_days = delta.days % 7` to get the remaining days after accounting for the full weeks.

We can also calculate the difference between two dates, which results in a `timedelta` object. The `timedelta` object represents the difference between two dates or times and can be used to perform arithmetic operations on dates.

```python

from datetime import timedelta

td = timedelta(days=29) # Create a timedelta of 29 days; A timedelta of 29 days represents a duration of 29 days.
d1 = date(2024, 6, 1)
print(d1 + td)  # Output: 2024-06-30
print(d1 - td)  # Output: 2024-05-03

```

Python handles the calendar correctly, so adding 29 days to June 1st results in June 30th, and subtracting 29 days from June 1st results in May 3rd.

### ISO 8601 Format

The ISO 8601 format is a standardized way to represent dates and times. It uses the format `YYYY-MM-DD` for dates and `HH:MM:SS` for times. For example, June 1st, 2024 would be represented as `2024-06-01`.

To convert a date to ISO 8601 format, you can use the `isoformat()` method:

```python

from datetime import date
my_date = date(2024, 6, 1)
iso_date = my_date.isoformat()
print(iso_date)  # Output: 2024-06-01

```

### strftime()

The `strftime()` method is used to format a date or time object into a string representation based on a specified format.

```python
from datetime import date

d = date(2024, 6, 1)

print(d.strftime("%Y")) # Output: 2024

```

We can also use `strftime()` to format the date in different ways:

```python
from datetime import date

d = date(2024, 6, 1)

print(d.strftime("Year: %Y, Month: %B, Day: %d")) # Output: Year: 2024, Month: June, Day: 01

```

For formatting, `%Y` represents the year with century, `%m` represents the month as a zero-padded decimal number, `%B` represents the full month name, and `%d` represents the day of the month as a zero-padded decimal number, among other format codes. They are shown in the table below:

| Format Code | Description                                          | Example Output |
|-------------|------------------------------------------------------|----------------|
| `%Y`        | Year with century                                    | 2024           |
| `%y`        | Year without century                                 | 24             |
| `%m`        | Month as a zero-padded decimal number                | 06             |
| `%B`        | Full month name                                      | June           |
| `%d`        | Day of the month as a zero-padded decimal number     | 01             |
| `%j`        | Day of the year as a zero-padded decimal number      | 153            |
| `%H`        | Hour (24-hour clock) as a zero-padded decimal number | 14             |
| `%M`        | Minute as a zero-padded decimal number               | 30             |
| `%S`        | Second as a zero-padded decimal number               | 45             |
| `%a`        | Abbreviated weekday name                             | Sat            |
| `%A`        | Full weekday name                                    | Saturday       |

```python

# Format YYYY/MM/DD
print(d.strftime("%Y/%m/%d")) # Output: 2024/06/01

```

## Combining Dates and Times

We can combine date and time objects to create a `datetime` object, which represents a specific point in time.

```python

from datetime import datetime

dt = datetime(2024, 6, 1, 14, 30, 45) # The format is datetime(year, month, day, hour, minute, second) and should be whole numbers.
print(dt)  # Output: 2024-06-01 14:30:45

```

In case we may want to add decimal places, we can add microseconds to the `datetime` object:

```python

from datetime import datetime

dt = datetime(2024, 6, 1, 14, 30, 45, 123456) # The format is datetime(year, month, day, hour, minute, second, microsecond) and should be whole numbers.
print(dt)  # Output: 2024-06-01 14:30:45.123456

```

We can also make new datetimes from existing ones by using the `replace()` method:

```python

from datetime import datetime

dt1 = datetime(2024, 6, 1, 14, 30, 45)
dt2 = dt1.replace(year=2025, month=7, day=2, hour=15, minute=45, second=30)
print(dt2)  # Output: 2025-07-02 15:45:30

```

Just like with date objects, we can format the `datetime` object in a custom print statement

```python

from datetime import datetime

dt = datetime(2024, 6, 1, 14, 30, 45)

print(dt.strftime("Year: %Y, Month: %B, Day: %d, Hour: %H, Minute: %M, Second: %S"))
# Output: Year: 2024, Month: June, Day: 01, Hour: 14, Minute: 30, Second: 45

```

and also convert it to ISO 8601 format:

```python

from datetime import datetime

dt = datetime(2024, 6, 1, 14, 30, 45)
iso_dt = dt.isoformat()
print(iso_dt)  # Output: 2024-06-01T14:30:45

```

### strptime()

The `strptime()` method is used to parse a string representation of a date or time into a `datetime` object based on a specified format.

It takes two arguments: the string to be parsed and the format string that specifies how the string is formatted. The format string uses the same format codes as `strftime()`.

```python
from datetime import datetime

dt_string = "2024-06-01 14:30:45"
dt_format = "%Y-%m-%d %H:%M:%S"
dt = datetime.strptime(dt_string, dt_format)
print(dt)  # Output: 2024-06-01 14:30:45

```

Note: The format string must match the format of the input string exactly, otherwise a `ValueError` will be raised.

We may also encounter `unix timestamps`, which represent the number of seconds that have elapsed since January 1, 1970 (UTC). We can convert a unix timestamp to a `datetime` object using the `fromtimestamp()` method:

```python
from datetime import datetime

ts = 1712137845
dt = datetime.fromtimestamp(ts)
print(dt)  # Output: 2024-04-03 12:50:45

```

We can also perform arithmetic operations on `datetime` objects using `timedelta`:

```python

from datetime import datetime, timedelta

start = datetime(2024, 6, 1, 14, 30, 45)
end = datetime(2024, 6, 15, 16, 45, 30)
duration = end - start
print(duration)  # Output: 14 days, 2:14:45
print(duration.total_seconds())  # Output: 1217685.0

```

We can also add a `timedelta` to a `datetime` object to get a new `datetime`:

```python

from datetime import datetime, timedelta

dt = datetime(2024, 6, 1, 14, 30, 45)
delta = timedelta(seconds=1000)

print(dt + delta)  # Output: 2024-06-01 14:47:25
print(dt - delta)  # Output: 2024-06-01 14:14:05

delta2 = timedelta(days=1, hours=2, minutes=30)
print(dt + delta2)  # Output: 2024-06-02 17:00:45
print(dt - delta2)  # Output: 2024-05-31 12:00:45

delta3 = timedelta(weeks=-1)
print(dt + delta3)  # Output: 2024-05-25 14:30:45
print(dt - delta3)  # Output: 2024-06-08 14:30:45

```

## Time Zones and Daylight Saving Time

The world operates across different time zones, and many regions observe daylight saving time (DST) to make better use of daylight during certain periods of the year. The United Kingdom was the first to standardize its time zone in 1847, and since then, many countries have adopted their own time zones relative to the original historical UK standard time, also known as Coordinated Universal Time (UTC) or earlier, Greenwich Mean Time (GMT).

So, the clocks west of the UK are set earlier than UTC, while the clocks east of the UK are set later than UTC. For example, New York is in the Eastern Time Zone (UTC-5), while Tokyo is in the Japan Standard Time Zone (UTC+9).

Python's `datetime` module provides support for time zones through the `pytz` library, which allows you to work with time zones and handle DST transitions.

```python

from datetime import datetime, timedelta, timezone

# US Eastern Standard Time (UTC-5)
ET = timezone(timedelta(hours=-5))

# Timezone-aware datetime in US Eastern Time
dt = datetime(2024, 6, 1, 14, 30, 45, tzinfo=ET)
print(dt)  # Output: 2024-06-01 14:30:45-05:00

```

Suppose we want to know what the date and time would have been if the clock had been set to India Standard Time (UTC+5:30) instead of US Eastern Time. We can convert the timezone-aware datetime to the new timezone using the `astimezone()` method:

```python

from datetime import datetime, timedelta, timezone

# India Standard Time (UTC+5:30)
IST = timezone(timedelta(hours=5, minutes=30))

# Timezone-aware datetime in US Eastern Time
print(dt.astimezone(IST))  # Output: 2024-06-02 01:00:45+05:30

```

There is an important difference between adjusting timezones and changing the `tzinfo` directly. We can set the `tzinfo` directly, using the `replace()` method. However, this does not adjust the time to the new timezone; it simply changes the timezone information without modifying the actual time. 

If we adjust into UTC with `astimezone()`, we change both the UTC offset and the clock itself. If we change the timezone with `replace()`, we change the UTC offset but not the clock itself.

```python

from datetime import datetime, timedelta, timezone

dt = datetime(2024, 6, 1, 14, 30, 45)

print(dt) # Output: 2024-06-01 14:30:45

# Adjusting timezone with astimezone()
print(dt.replace(tzinfo=timezone.utc)) # Output: 2024-06-01 14:30:45+00:00

# Adjusting timezone with replace() - Changing original time to match the new timezone
print(dt.astimezone(timezone.utc)) # Output: 2024-06-01 11:30:45+00:00
```

Since the world is divided into many time zones, and some regions observe daylight saving time, it can be complex to handle time zone conversions and DST transitions correctly. The `pytz` library provides a comprehensive database of time zones and handles these complexities for you.

The database, `tz`, is usually updated 3-4 times a year as timezone rules change. It is used by computer programs across many programming languages. Since timezone information changes so quickly, it does not make sense to bundle it directly into Python. Instead, we use a package called `dateutil` that provides an interface to the `tz` database.

```python

from datetime import datetime
from dateutil import tz

# Eastern Time Zone
et = tz.gettz('America/New_York') # Format: 'Continent/City'

d1 = datetime(2024, 6, 1, 14, 30, 45, tzinfo=et)
print(d1)  # Output: 2024-06-01 14:30:45-04:00

```

In places where daylight saving time is observed, the UTC offset changes during the year. For example, in New York, the UTC offset is -5 hours during standard time and -4 hours during daylight saving time. The `dateutil` library automatically handles these transitions based on the date and time.

```python

from datetime import datetime
from dateutil import tz

spring_ahead_159am = datetime(2024, 3, 10, 1, 59, 59)
print(spring_ahead_159am.isoformat())  # Output: 2024-03-10T01:59:59
spring_ahead_2am = datetime(2024, 3, 10, 3, 0, 0)
print(spring_ahead_2am.isoformat())  # Output: 2024-03-10T02:00:00

# Difference
print((spring_ahead_2am - spring_ahead_159am).total_seconds())  # Output: 3601.0 - 1 hour and 1 second apart

```

```python

from datetime import datetime, timedelta, timezone

EST = timezone(timedelta(hours=-5))
EDT = timezone(timedelta(hours=-4))

spring_ahead_159am = datetime(2024, 3, 10, 1, 59, 59, tzinfo=EST)
print(spring_ahead_159am.isoformat())  # Output: 2024-03-10T01:59:59-05:00
spring_ahead_2am = datetime(2024, 3, 10, 3, 0, 0, tzinfo=EDT)
print(spring_ahead_2am.isoformat())  # Output: 2024-03-10T03:00:00-04:00

# Difference
print((spring_ahead_2am - spring_ahead_159am).total_seconds()) # Output: 1.0 - 1 second apart

```

Putting things in terms of UTC can help avoid confusion when dealing with time zones and daylight saving time. UTC does not observe daylight saving time, so the UTC offset remains constant throughout the year. By converting all times to UTC, you can ensure that you are working with a consistent time reference regardless of the local time zone or DST rules.

When ending daylight saving time, the clock is set back one hour, resulting in a repeated hour. For example, in New York, the clock goes back from 2:00 AM to 1:00 AM on the first Sunday in November. This means that the hour from 1:00 AM to 2:00 AM occurs twice, once in EDT and once in EST.

```python

from datetime import datetime
from dateutil import tz

eastern = tz.gettz('US/Eastern')

# 2017-11-05 01:00:00
first_1_am = datetime(2017, 11, 5, 1, 0, 0, tzinfo=eastern)
tz.datetime_ambiguous(first_1_am) # Output: True - This time is ambiguous because it occurs twice during the transition from daylight saving time to standard time.

# 2017-11-05 01:00:00
second_1_am = datetime(2017, 11, 5, 1, 0, 0, tzinfo=eastern)
second_1_am = tz.enfold(second_1_am) # Mark the second occurrence of 1:00 AM as the "folded" time, which indicates that it is the second occurrence of the ambiguous time.
tz.datetime_ambiguous(second_1_am) # Output: False - This time is not ambiguous because it has been marked as the second occurrence of the ambiguous time.

print(first_1_am - second_1_am) # Output: 0:00:00 - The difference between the two times is zero because they represent the same point in time, just with different timezone information.

# Converting to UTC
first_1_am_utc = first_1_am.astimezone(tz.UTC)
second_1_am_utc = second_1_am.astimezone(tz.UTC)

print(first_1_am_utc)  # Output: 2017-11-05 05:00:00+00:00 - The first occurrence of 1:00 AM in US Eastern Time corresponds to 5:00 AM in UTC because it is during daylight saving time (EDT, UTC-4).
print(second_1_am_utc) # Output: 2017-11-05 06:00:00+00:00 - The second occurrence of 1:00 AM in US Eastern Time corresponds to 6:00 AM in UTC because it is during standard time (EST, UTC-5).
print(second_1_am_utc - first_1_am_utc) # Output: 1:00:00 - The difference between the two UTC times is one hour because they represent different points in time due to the transition from daylight saving time to standard time.

```

## Dates and Times in Pandas

To make timedelta columns, we have to first convert the date columns to datetime objects using `pd.to_datetime()`, and then we can subtract the two datetime columns to get a timedelta column.

We can also use the `parse_dates` parameter in `pd.read_csv()` to automatically parse date columns when reading a CSV file.

```python

import pandas as pd

rides = pd.read_csv('rides.csv', parse_dates=['start_time', 'end_time'])

# Or

import pandas as pd

rides = pd.read_csv('rides.csv')
rides['start_time'] = pd.to_datetime(rides['start_time'])
rides['end_time'] = pd.to_datetime(rides['end_time'])

rides['duration'] = rides['end_time'] - rides['start_time']
print(rides['duration'])

```

We can then add custom columns to the DataFrame based on the duration, such as the number of minutes or hours. There are various attributes and methods available for working with datetime and timedelta objects in pandas. Some are listed below:

- `dt` accessor: This allows you to access datetime properties and methods for a Series of datetime objects. For example, `rides['start_time'].dt.year` would give you the year component of the start time.

- `total_seconds()`: This method can be used on a timedelta object to get the total duration in seconds. For example, `rides['duration'].dt.total_seconds()` would give you the duration of each ride in seconds.

- `components`: This attribute can be used on a timedelta object to get the duration broken down into its components (days, hours, minutes, seconds). For example, `rides['duration'].dt.components` would give you a DataFrame with the components of the duration for each ride.


## DateTime Properties and Attributes

| Property | Description |
|----------|-------------|
| year | The year of the datetime |
| month | The month of the datetime |
| day | The days of the datetime |
| hour | The hour of the datetime |
| minute | The minutes of the datetime |
| second | The seconds of the datetime |
| microsecond | The microseconds of the datetime |
| nanosecond | The nanoseconds of the datetime |
| date | Returns datetime.date (does not contain timezone information) |
| time | Returns datetime.time (does not contain timezone information) |
| timetz | Returns datetime.time as local time with timezone information |
| dayofyear | The ordinal day of year |
| day_of_year | The ordinal day of year |
| dayofweek | The number of the day of the week with Monday=0, Sunday=6 |
| day_of_week | The number of the day of the week with Monday=0, Sunday=6 |
| weekday | The number of the day of the week with Monday=0, Sunday=6 |
| quarter | Quarter of the date: Jan-Mar = 1, Apr-Jun = 2, etc. |
| days_in_month | The number of days in the month of the datetime |
| is_month_start | Logical indicating if first day of month (defined by frequency) |
| is_month_end | Logical indicating if last day of month (defined by frequency) |
| is_quarter_start | Logical indicating if first day of quarter (defined by frequency) |
| is_quarter_end | Logical indicating if last day of quarter (defined by frequency) |
| is_year_start | Logical indicating if first day of year (defined by frequency) |
| is_year_end | Logical indicating if last day of year (defined by frequency) |
| is_leap_year | Logical indicating if the date belongs to a leap year |

## Date Offsets and Frequency Strings

Most DateOffsets have associated frequencies strings, or offset aliases, that can be passed into freq keyword arguments. The available date offsets and associated frequency strings can be found below:

| Date Offset | Frequency String | Description |
|-------------|------------------|-------------|
| DateOffset | None | Generic offset class, defaults to absolute 24 hours |
| BDay or BusinessDay | 'B' | business day (weekday) |
| CDay or CustomBusinessDay | 'C' | custom business day |
| Week | 'W' | one week, optionally anchored on a day of the week |
| WeekOfMonth | 'WOM' | the x-th day of the y-th week of each month |
| LastWeekOfMonth | 'LWOM' | the x-th day of the last week of each month |
| MonthEnd | 'ME' | calendar month end |
| MonthBegin | 'MS' | calendar month begin |
| BMonthEnd or BusinessMonthEnd | 'BME' | business month end |
| BMonthBegin or BusinessMonthBegin | 'BMS' | business month begin |
| CBMonthEnd or CustomBusinessMonthEnd | 'CBME' | custom business month end |
| CBMonthBegin or CustomBusinessMonthBegin | 'CBMS' | custom business month begin |
| SemiMonthEnd | 'SME' | 15th (or other day_of_month) and calendar month end |
| SemiMonthBegin | 'SMS' | 15th (or other day_of_month) and calendar month begin |
| QuarterEnd | 'QE' | calendar quarter end |
| QuarterBegin | 'QS' | calendar quarter begin |
| BQuarterEnd | 'BQE' | business quarter end |
| BQuarterBegin | 'BQS' | business quarter begin |
| FY5253Quarter | 'REQ' | retail (aka 52-53 week) quarter |
| HalfYearEnd | 'HYE' | calendar half year end |
| HalfYearBegin | 'HYS' | calendar half year begin |
| BHalfYearEnd | 'BHYE' | business half year end |
| BHalfYearBegin | 'BHYS' | business half year begin |
| YearEnd | 'YE' | calendar year end |
| YearBegin | 'YS' or 'BYS' | calendar year begin |
| BYearEnd | 'BYE' | business year end |
| BYearBegin | 'BYS' | business year begin |
| FY5253 | 'RE' | retail (aka 52-53 week) year |
| Easter | None | Easter holiday |
| BusinessHour | 'bh' | business hour |
| CustomBusinessHour | 'cbh' | custom business hour |
| Day | 'D' | one calendar day |
| Hour | 'h' | one hour |
| Minute | 'min' | one minute |
| Second | 's' | one second |
| Milli | 'ms' | one millisecond |
| Micro | 'us' | one microsecond |
| Nano | 'ns' | one nanosecond |

There are also some useful techniques such as resampling, which is a method for converting a time series to a different frequency. For example, you can resample daily data to monthly data by taking the mean of each month.

```python

import pandas as pd

# Create a sample time series with daily frequency
rides.resample('M', on='start_time').size() # Resample the rides DataFrame to monthly frequency based on the 'start_time' column and count the number of rides in each month.

```

We can resample on day level, weekly, month end, or year end. The frequencies used are shown in the table above. Resampling can be used to perform various operations such as calculating the mean, sum, or count of values within each resampled period. It is a powerful technique for analyzing time series data at different levels of granularity.

### Time Zone Handling in Pandas

Pandas provides robust support for time zone handling through the `tz` attribute of datetime-like objects. You can use the `tz_localize()` method to set the time zone for a datetime column and the `tz_convert()` method to convert between time zones.

```python

import pandas as pd

rides['start_time'] = rides['start_time'].dt.tz_localize('UTC') # Localize the 'start_time' column to UTC

# Convert the 'start_time' column to US Eastern Time
rides['start_time'] = rides['start_time'].dt.tz_convert('US/Eastern')

```

In case we get an error about ambiguous times during daylight saving time transitions, we can use the `ambiguous` parameter to specify how to handle these cases. For example, we can set `ambiguous='NaT'` to mark ambiguous times as Not a Time (NaT):

```python

import pandas as pd

rides['start_time'] = rides['start_time'].dt.tz_localize('US/Eastern', ambiguous='NaT') # Localize the 'start_time' column to US Eastern Time, marking ambiguous times as NaT

```

This will help ensure that your time zone handling is accurate and that you can work with time series data effectively in pandas.

If we remove the ambiguous times, it is important we shift the indexes to fill in the missing times. We can use the `shift()` method to shift the index by a specified number of periods.

```python

import pandas as pd

# Shift the index by one period to fill in the missing times
rides.index = rides.index.shift(1, freq='H') # Shift the index of the rides DataFrame by one hour to fill in the missing times after removing ambiguous times.

```

More pandas time and date handling techniques can be found in the official pandas documentation: [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html#)