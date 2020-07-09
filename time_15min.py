import math

a = int(input())
b = int(input())
hr = a * 60  # min
ttlmin = hr + b + 15  # min
hrs = math.floor(ttlmin / 60)  # hr
min = ttlmin % 60
if hrs == 24:
    hrs = 0
if min < 10:
    print(f'{hrs}:0{min}')
else:
    print(f'{hrs}:{min}')