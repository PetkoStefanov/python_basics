time_first = float(input())
time_second = float(input())
time_third = float(input())

time_seconds = time_first + time_second + time_third
time_minutes = time_seconds // 60

time_seconds_left = time_seconds % 60
if time_seconds_left < 10:
    print("%d" % time_minutes + ":" + "0%.d" % time_seconds_left)
else:
    print("%d" % time_minutes + ":" + "%d" % time_seconds_left)
