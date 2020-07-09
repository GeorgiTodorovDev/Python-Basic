money_for_vacation = float(input())
money_we_have = float(input())
spend_counter = 0
day_counter = 0
while money_we_have < money_for_vacation and spend_counter < 5:
    action = input()
    saved_money = float(input())
    day_counter += 1
    if action == "save":
        money_we_have += saved_money
        spend_counter = 0
    elif action == "spend":
        money_we_have -= saved_money
        spend_counter += 1
        if money_we_have < 0:
            money_we_have = 0

if spend_counter >= 5:
    print(f"You can't save the money.\n{day_counter}")

if money_we_have >= money_for_vacation:
    print(f"You saved the money for {day_counter} days.")