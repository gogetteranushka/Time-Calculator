def add_time(start, duration, start_day=None):
    # Parse start time
    start_time, meridiem = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if meridiem == 'PM':
        start_hour += 12

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate new time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Handle overflow in minutes
    if new_minute >= 60:
        new_minute -= 60
        new_hour += 1

    # Handle overflow in hours
    new_day_count = new_hour // 24
    new_hour %= 24

    # Determine meridiem
    if new_hour >= 12:
        new_meridiem = 'PM'
        if new_hour > 12:
            new_hour -= 12
    else:
        new_meridiem = 'AM'
        if new_hour == 0:
            new_hour = 12

    # Format the new time
    new_time = f"{new_hour}:{new_minute:02d} {new_meridiem}"

    # Calculate new day of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if start_day:
        start_day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (start_day_index + new_day_count) % 7
        new_day = days_of_week[new_day_index]
        new_time += f', {new_day}'

    # Add indication for the next day or days later
    if new_day_count == 1:
        new_time += ' (next day)'
    elif new_day_count > 1:
        new_time += f' ({new_day_count} days later)'

    return new_time
