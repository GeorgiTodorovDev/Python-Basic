strawberry_price = float(input())
banana_qu_in_kg = float(input())
orange_qu_in_kg = float(input())
raspberry_qu_in_kg = float(input())
strawberry_qu_in_kg = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price - (raspberry_price * 0.40)
banana_price = raspberry_price - (raspberry_price * 0.80)

raspberry_final_price = raspberry_qu_in_kg * raspberry_price
orange_final_price = orange_price * orange_qu_in_kg
banana_final_price = banana_price * banana_qu_in_kg
strawberry_final_price = strawberry_qu_in_kg * strawberry_price

result = raspberry_final_price + orange_final_price + banana_final_price + strawberry_final_price
print(result)