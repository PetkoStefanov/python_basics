hours = float(input()) * 60
minutes = float(input())

all_time = hours + minutes + 15

time_hours = all_time // 60

time_minutes = all_time % 60

if time_hours >= 24:
    time_hours -= 24
    if time_minutes < 10:
        print("%d" % time_hours + ":" + "0%.d" % time_minutes)
    else:
        print("%d" % time_hours + ":" + "%d" % time_minutes)
else:
    if time_minutes < 10:
        print("%d" % time_hours + ":" + "0%.d" % time_minutes)
    else:
        print("%d" % time_hours + ":" + "%d" % time_minutes)
