deposit_amount = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())

interest = deposit_amount * ( annual_interest_rate / 100 )
interest_for_month = interest / 12
result = deposit_amount + ( term_of_the_deposit * interest_for_month )

print(result)