length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_of_tank = length * width * height
max_liters = volume_of_tank * 0.001
perc = percentage * 0.01

result = max_liters * (1 - perc)
print(result)