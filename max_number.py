import sys
max_num = -sys.maxsize
command = input()
while command != "Stop":
    n = int(command)
    if n > max_num:
        max_num = n
    command = input()
print(max_num)