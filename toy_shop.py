trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

ttl_cost = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
ttl_toys = puzzles + dolls + bears + minions + trucks
if ttl_toys >= 50:
    discount = ttl_cost * 0.25
    ttl_cost -= discount
rent = ttl_cost * 0.1
profit = ttl_cost - rent
if profit >= trip:
    print(f'Yes! {abs(profit - trip):.2f} lv left.')
elif profit < trip:
    print(f'Not enough money! {abs(profit - trip):.2f} lv needed.')