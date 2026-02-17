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

## Dates and Times in Pandas