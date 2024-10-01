from datetime import datetime, timedelta, timezone

# Create a datetime object
dt = datetime(2024, 10, 30, 14, 30, 45)

# Get the current date and time
current_dt = datetime.now()

# Format the datetime object
formatted_dt = dt.strftime("%y-%m-%d")

# Parse a string into a datetime object
date_str = "24-10-30 14:30:45"
parsed_dt = datetime.strptime(date_str, "%y-%m-%d %H:%M:%S")

# Add 10 days to the datetime object
new_dt = dt + timedelta(days=10)

# Compare datetime objects
is_earlier = dt < new_dt

# Extract components
year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
minute = dt.minute
second = dt.second

# Handle timezones
utc_dt = datetime(2024, 10, 30, 14, 30, 45, tzinfo=timezone.utc)

print(f"Original datetime: {dt}")
print(f"Current datetime: {current_dt}")
print(f"Formatted datetime: {formatted_dt}")
print(f"Parsed datetime: {parsed_dt}")
print(f"New datetime (10 days later): {new_dt}")
print(f"Is original datetime earlier than new datetime? {is_earlier}")
print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {
      hour}, Minute: {minute}, Second: {second}")
print(f"UTC datetime: {utc_dt}")
