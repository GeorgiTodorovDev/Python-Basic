tabs = int(input())
salary = int(input())



for i in range(tabs):
    num_sites = input()
    if num_sites == "Facebook":
        salary -= 150
    elif num_sites == "Instagram":
        salary -= 100
    elif num_sites == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
        print(f'{salary}')