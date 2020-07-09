day_from_week = str(input())
result = 0

if day_from_week == "Monday" or day_from_week == "Tuesday" or \
    day_from_week == "Friday":
    result = 12
elif day_from_week == "Wednesday" or day_from_week == "Thursday":
    result = 14
else:
    result = 16

print(result)