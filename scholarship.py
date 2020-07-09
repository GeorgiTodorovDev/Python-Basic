import math

income = float(input())
avr = float(input())
min_salary = float(input())
social = 0.0
grade = 0.0
if income <= min_salary and avr >= 4.5:
    social = math.floor(min_salary * 0.35)
if avr >= 5.5:
    grade = math.floor(avr * 25)
if social > grade:
    print(f'You get a Social scholarship {social} BGN')
elif social < grade:
    print(f'You get a scholarship for excellent results {grade} BGN')
else:
    print('You cannot get a scholarship!')