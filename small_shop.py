product = input()
city = input()
quantity = float(input())

result = 0.0

if city == "Sofia":
    if product == "coffee":
        result = quantity * 0.5
    elif product == "water":
        result = quantity * 0.8
    elif product == "beer":
        result = quantity * 1.2
    elif product == "sweets":
        result = quantity * 1.45
    else:
        result = quantity * 1.6
elif city == "Plovdiv":
    if product == "coffee":
        result = quantity * 0.4
    elif product == "water":
        result = quantity * 0.7
    elif product == "beer":
        result = quantity * 1.15
    elif product == "sweets":
        result = quantity * 1.30
    else:
        result = quantity * 1.5
else:
    if product == "coffee":
        result = quantity * 0.45
    elif product == "water":
        result = quantity * 0.7
    elif product == "beer":
        result = quantity * 1.1
    elif product == "sweets":
        result = quantity * 1.35
    else:
        result = quantity * 1.55

print(result)
