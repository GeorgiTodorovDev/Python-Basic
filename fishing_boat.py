budget = int(input())
season = input()
fisherman_num = int(input())

# "Spring", "Summer", "Autumn" или "Winter";
"""
В зависимост от сезона:
    • Цената за наем на кораба през пролетта е  3000 лв.;
    • Цената за наем на кораба през лятото и есента е  4200 лв.;
    • Цената за наем на кораба през зимата е  2600 лв.
В зависимост от броя на групата има различна отстъпка:
    • Ако групата е до 6 човека включително  –  отстъпка от 10%;
    • Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
    • Ако групата е от 12 нагоре  –  отстъпка от 25%.
    
        • Ако бюджетът е достатъчен:
"Yes! You have {останалите пари} leva left."
    • Ако бюджетът НЕ Е достатъчен:
"Not enough money! You need {сумата, която не достига} leva."

3000
Summer
11
Лятото риболовния туризъм струва 4200 лв., 11 рибари ползват 15% отстъпка -> 4200 - 15% = 3570 лв., нечетен брой са и не ползват допълнителна отстъпка,
3000 <= 3570, следователно не им достигат 570.00 лв.
"""
total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Summer" or season == "Autumn":
    total_price = 4200
elif season == "Winter":
    total_price = 2600

if fisherman_num <= 6:
    total_price -= total_price * 0.1
elif 7 <= fisherman_num <= 11:
    total_price -= total_price * 0.15
elif fisherman_num > 11:
    total_price -= total_price * 0.25

if (fisherman_num % 2 == 0) and (not season == "Autumn"):
    total_price -= total_price * 0.05

diff = total_price - budget

if total_price > budget:
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    print(f'Yes! You have {abs(diff):.2f} leva left.')