days_for_campaign = int(input())
num_of_cooks = int(input())
num_of_cakes = int(input())
num_of_waffles = int(input())
num_of_pancakes = int(input())

cake_price_for_day = num_of_cakes * 45
waffles_price_for_day = num_of_waffles * 5.80
pancakes_price_for_day = num_of_pancakes * 3.20

total_price_for_day = (cake_price_for_day + waffles_price_for_day + pancakes_price_for_day) * num_of_cooks
total_price = total_price_for_day * days_for_campaign

result = total_price - (total_price / 8)
print(f'{result:.2f}')
