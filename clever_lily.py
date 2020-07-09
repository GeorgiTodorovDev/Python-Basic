age = int(input())
wash_price = float(input())
toy_price = int(input())
ttl_money = 0
money = 0
toy = 0
for i in range(1, age+1):
    if i % 2 == 0:
        money += 10
        ttl_money += money - 1
    elif i % 2 != 0:
        toy += 1
ttl_money += toy * toy_price
if ttl_money >= wash_price:
    print(f'Yes! {abs(ttl_money - wash_price):.2f}')
else:
    print(f'No! {abs(ttl_money - wash_price):.2f}')