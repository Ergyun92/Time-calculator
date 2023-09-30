def add_time(start, duration, day=""):
    week_days = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }

# Separating the time into parts
    start_time = start.partition(":")
    start_hours = int(start_time[0])
    start_time2 = start_time[2].partition(" ")
    start_minutes = int(start_time2[0])
    am_or_pm = start_time2[2]
    duration_time = duration.partition(":")
    duration_hours = int(duration_time[0])
    duration_minutes = int(duration_time[2])

# Making sure we don't pass the 12h/60m marks
    start_minutes_total = (start_hours * 60) + start_minutes
    duration_minutes_total = (duration_hours * 60) + duration_minutes
    total_minutes = start_minutes_total + duration_minutes_total

    days_passed = total_minutes // 60 // 24
    end_hours = total_minutes // 60 % 24
    end_minutes = total_minutes % 60
    if end_minutes > 59:
        end_hours += 1  

# Keeping track of PM and AM
    if end_hours == 12 and am_or_pm == "PM":
        end_hours = 12
        am_or_pm = "AM"
        days_passed += 1
    elif end_hours > 12 and am_or_pm == "PM":
        end_hours = end_hours - 12
        am_or_pm = "AM"
        days_passed += 1
    elif end_hours < 12 and am_or_pm == "PM":
        end_hours = end_hours
        am_or_pm = "PM"
    elif end_hours == 12 and am_or_pm == "AM":
        end_hours = 12
        am_or_pm = "PM"
    elif end_hours > 12 and am_or_pm == "AM":
        end_hours = end_hours - 12
        am_or_pm = "PM"
    elif end_hours < 12 and am_or_pm == "AM":
        end_hours = end_hours
        am_or_pm = "AM"
    elif end_hours == 0 and am_or_pm == "AM":
        end_hours = 12
        am_or_pm = "PM"
    elif end_hours == 12 and am_or_pm == "PM":
        end_hours = 12
        am_or_pm = "AM"
        days_passed += 1
# Correcting visualisation of minutes
    if end_minutes < 10:
        end_minutes = "0" + str(end_minutes)
    else:
        end_minutes = end_minutes
# Getting the new time
    show_day = ""
    new_time = f"{end_hours}:{end_minutes} {am_or_pm}"
    if not day:
        if days_passed == 0:
            return new_time
        elif days_passed == 1:
            return f"{new_time} (next day)"
        else:
            return f"{new_time} ({days_passed} days later)"
    else:
        day = day.capitalize()
        end_day = (week_days[day] + days_passed) % 7
        for (key, value) in week_days.items():
            if end_day == value:
                show_day = key
        if days_passed == 0:
            return f"{new_time}, {show_day}"
        elif days_passed == 1:
            return f"{new_time}, {show_day} (next day)"
        else:
            return f"{new_time}, {show_day} ({days_passed} days later)"
      