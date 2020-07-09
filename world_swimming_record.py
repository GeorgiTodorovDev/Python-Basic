import math

rec_in_sec = float(input())
dist_in_m = float(input())
time_in_sec = float(input())
dist_in_sec = time_in_sec * dist_in_m
delay = math.floor(dist_in_m / 15) * 12.5
ttl_time = dist_in_sec + delay
if ttl_time < rec_in_sec:
    print(f'Yes, he succeeded! The new world record is {ttl_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(ttl_time - rec_in_sec):.2f} seconds slower.')