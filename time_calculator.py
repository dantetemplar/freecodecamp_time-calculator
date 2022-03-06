import re

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def add_time(start, duration, weekday=""):
    hours, minutes, meridiem = re.search(r'(\d{1,2}):(\d{1,2}) (PM|AM)', start).groups()
    hours, minutes = int(hours), int(minutes)
    delta_hours, delta_minutes = map(int, re.search(r'(\d*):(\d*)', duration).groups())

    add_hours, minutes = divmod(minutes + delta_minutes, 60)
    add_days, hours = divmod(hours + delta_hours + add_hours + (12 if meridiem == 'PM' else 0), 24)

    if add_days == 0:
        days_passed = ""
    elif add_days == 1:
        days_passed = "next day"
    else:
        days_passed = f"{add_days} days later"

    weekday = weekdays[(weekdays.index(weekday.capitalize()) + add_days) % 7] if weekday else None
    meridiem, hours = divmod(hours, 12)

    r = f"{12 if hours == 0 else hours:d}:{minutes:02d} " + \
        ('PM' if meridiem else 'AM') + \
        (f", {weekday}" if not weekday is None else '') + \
        (f" ({days_passed})" if days_passed else '')

    return r

if __name__ == '__main__':
    print(add_time("11:59 PM", "24:05", "Wednesday"))
