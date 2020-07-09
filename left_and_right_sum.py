n = int(input())

left = 0
right = 0

for i in range(n):
    left += int(input())

for i in range(n):
    right += int(input())

if left == right:
    print(f"Yes, sum = {left}")
else:
    print(f"No, diff = {abs(left - right)}")