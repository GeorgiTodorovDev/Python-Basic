hour = int(input())
day_from_week = input()

result = ""

if day_from_week == "Sunday":
    result = "closed"
else:
    if 10 <= hour <= 18:
        result = "open"
    else:
        result = "closed"

print(result)
