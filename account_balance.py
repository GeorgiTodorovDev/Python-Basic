insert = input()
sum = 0.0
while insert != "NoMoreMoney":
    amount = float(insert)
    if amount < 0:
        print("Invalid operation!")
        break

    sum += amount
    print(f'Increase: {amount:.2f}')
    insert = input()
print(f'Total: {sum:.2f}')