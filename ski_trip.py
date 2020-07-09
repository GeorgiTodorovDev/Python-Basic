days_for_staying = int(input())
type_of_room = input()
evaluation = input()

nights_used = 0
result = 0.0

nights_used = days_for_staying - 1

if type_of_room == "room for one person":
        result = nights_used * 18
elif type_of_room == "apartment":
    if days_for_staying == 1:
        result = nights_used * 25
    elif 1 < days_for_staying < 10:
        result = (nights_used * 25) - ((nights_used * 25) * 0.30)
    elif 10 <= days_for_staying <= 15:
        result = (nights_used * 25) - ((nights_used * 25) * 0.35)
    elif days_for_staying > 15:
        result = (nights_used * 25) - ((nights_used * 25) * 0.50)
elif type_of_room == "president apartment":
    if days_for_staying == 1:
        result = nights_used * 35
    elif 1 < days_for_staying < 10:
        result = (nights_used * 35) - ((nights_used * 35) * 0.10)
    elif 10 <= days_for_staying <= 15:
        result = (nights_used * 35) - ((nights_used * 35) * 0.15)
    elif days_for_staying > 15:
        result = (nights_used * 35) - ((nights_used * 35) * 0.20)

if evaluation == "positive":
    result += result * 0.25
else:
    result -= result * 0.10

print(f'{result:.2f}')