flower_type = input()
count_flowers = int(input())
budget = int(input())

price_per_flower = 0.0

#"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
#  5         3.80      2.80        3              2.50

if flower_type == "Roses":
    price_per_flower = 5
    if count_flowers > 80:
        price_per_flower -= price_per_flower * 0.10
elif flower_type == "Dahlias":
    price_per_flower = 3.80
    if count_flowers > 90:
        price_per_flower -= price_per_flower * 0.15
elif flower_type == "Tulips":
    price_per_flower = 2.80
    if count_flowers > 80:
        price_per_flower -= price_per_flower * 0.15
elif flower_type == "Narcissus":
    price_per_flower = 3
    if count_flowers < 120:
        price_per_flower += price_per_flower * 0.15
elif flower_type == "Gladiolus":
    price_per_flower = 2.50
    if count_flowers < 80:
        price_per_flower += price_per_flower * 0.20

total_price = count_flowers * price_per_flower

diff = total_price - budget

if total_price > budget:
    print(f'Not enough money, you need {diff:.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {count_flowers} {flower_type} and {abs(diff):.2f} leva left.')