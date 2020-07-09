import sys
max_num = -sys.maxsize
sum_numbers = 0

n = int(input())

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_numbers += num

sum_numbers -= max_num
if sum_numbers == max_num:
    print(f'Yes\nSum = {sum_numbers}')
else:
    print(f'No\nDiff = {abs(max_num - sum_numbers)}')

