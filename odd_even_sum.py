n = int(input())

even = 0
odd = 0

for i in range(1, (n+1)):
    n2 = int(input())
    if i % 2 == 0:
        even += n2
    else:
        odd += n2

diff = even - odd
if even > odd:
    print(f'No\nDiff = {diff}')
elif even < odd:
    print(f'No\nDiff = {abs(diff)}')
elif even == odd:
    print(f'Yes\n Sum = {even}')
