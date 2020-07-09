import math

t1 = int(input())
t2 = int(input())
t3 = int(input())
ttl = t1 + t2 + t3
min = math.floor(ttl / 60)
sec = ttl % 60
if sec < 10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')