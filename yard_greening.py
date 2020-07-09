#    • "The final price is: {крайна цена на услугата} lv."
#    • "The discount is: {отстъпка} lv."
first_price = float(input()) * 7.61
discount = first_price * 0.18
final_price = first_price - discount
print(f'The final price is: {final_price:.2f} lv.\nThe discount is: {discount:.2f} lv.')