import sys
min_num = sys.maxsize
command = input()
while command != "Stop":
    n = int(command)
    if n < min_num:
        min_num = n
    command = input()
print(min_num)