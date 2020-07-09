fruit = input()
day_of_week = input()
quantity = float(input())

result = 0.0
error = False
#banana / apple / orange / grapefruit / kiwi / pineapple / grapes
#2.50 1.20 0.85 1.45 2.70 5.50 3.85
#2.70 1.25 0.90 1.60 3.00 5.60 4.20


if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
    or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        result = quantity * 2.50
    elif fruit == "apple":
        result = quantity * 1.20
    elif fruit == "orange":
        result = quantity * 0.85
    elif fruit == "grapefruit":
        result = quantity * 1.45
    elif fruit == "kiwi":
        result = quantity * 2.70
    elif fruit == "pineapple":
        result = quantity * 5.50
    elif fruit == "grapes":
        result = quantity * 3.85
    else:
        error = True
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        result = quantity * 2.70
    elif fruit == "apple":
        result = quantity * 1.25
    elif fruit == "orange":
        result = quantity * 0.90
    elif fruit == "grapefruit":
        result = quantity * 1.60
    elif fruit == "kiwi":
        result = quantity * 3.00
    elif fruit == "pineapple":
        result = quantity * 5.60
    elif fruit == "grapes":
        result = quantity * 4.20
    else:
        error = True
else:
    error = True

if error == True:
    print("error")
else:
    print(f'{result:.2f}')

    