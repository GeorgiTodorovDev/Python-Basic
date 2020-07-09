n = int(input())

p2 = 0
p3 = 0
p4 = 0

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        p2 += 1
    if num % 3 == 0:
        p3 += 1
    if num % 4 == 0:
        p4 += 1

pp2 = p2 / n * 100
pp3 = p3 / n * 100
pp4 = p4 / n * 100

print(f'{pp2:.2f}%')
print(f'{pp3:.2f}%')
print(f'{pp4:.2f}%')