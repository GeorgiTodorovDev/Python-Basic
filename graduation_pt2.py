name = input()
year = 1
grade = 0
counter = 0
while year <= 12:
    grades = float(input())
    if grades < 4:
        counter += 1
        if counter >= 2:
            print(f'{name} has been excluded at {year - 1} grade')
            break
    year += 1
    grade += grades
if counter < 2:
    print(f'{name} graduated. Average grade: {(grade / (year-1)):.2f}')