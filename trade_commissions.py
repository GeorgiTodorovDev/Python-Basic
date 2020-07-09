city = input()
sales = float(input())
error = False
result = 0.0

if city == "Sofia":
    # noinspection PyUnreachableCode
    if 0 <= sales <= 500:
        result = sales * 0.05
    elif 500 < sales <= 1000:
        result = sales * 0.07
    elif 1000 < sales <= 10000:
        result = sales * 0.08
    elif sales > 10000:
        result = sales * 0.12
    else:
        error = True
elif city == "Varna":
    if 0 <= sales <= 500:
        result = sales * 0.045
    elif 500 < sales <= 1000:
        result = sales * 0.075
    elif 1000 < sales <= 10000:
        result = sales * 0.10
    elif sales > 10000:
        result = sales * 0.13
    else:
        error = True
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        result = sales * 0.055
    elif 500 < sales <= 1000:
        result = sales * 0.08
    elif 1000 < sales <= 10000:
        result = sales * 0.12
    elif sales > 10000:
        result = sales * 0.145
    else:
        error = True
else:
    error = True

if error == True:
    print("error")
else:
    print(f'{result:.2f}')