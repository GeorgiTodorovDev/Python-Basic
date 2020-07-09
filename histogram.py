n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for i in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    else:
        p5 += 1

p1_pr = p1 / n * 100
p2_pr = p2 / n * 100
p3_pr = p3 / n * 100
p4_pr = p4 / n * 100
p5_pr = p5 / n * 100

print(f'{p1_pr:.2f}%')
print(f'{p2_pr:.2f}%')
print(f'{p3_pr:.2f}%')
print(f'{p4_pr:.2f}%')
print(f'{p5_pr:.2f}%')