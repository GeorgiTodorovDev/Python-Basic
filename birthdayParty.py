rent_for_house = int(input())

cake = rent_for_house * (20 / 100)
drinks = cake - (cake * 0.45)
animators = rent_for_house / 3

result = rent_for_house + cake + drinks + animators

print(result)