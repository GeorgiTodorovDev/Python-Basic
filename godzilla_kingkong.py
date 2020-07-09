budget = float(input())
statists = int(input())
cloth_price = float(input())
cloth_cost = cloth_price * statists
decor = budget * 0.1
if statists >= 150:
    discount = cloth_cost * 0.1
    cloth_cost = cloth_cost - discount
ttl = decor + cloth_cost
if ttl <= budget:
    print('Action!')
    print(f'Wingard starts filming with {abs(ttl - budget):.2f} leva left.')
elif ttl > budget:
    print('Not enough money!')
    print(f'Wingard needs {abs(ttl - budget):.2f} leva more.')