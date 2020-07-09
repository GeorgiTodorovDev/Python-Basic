text = str(input())
if text == 'square':
    a = float(input())
    area = a * a
    print(f'{area:.3f}')
if text == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
if text == 'circle':
    a = float(input())
    import math
    area = math.pi * pow(a, 2)
    print(f'{area:.3f}')
if text == 'triangle':
    a = float(input())
    b = float(input())
    area = a * b / 2
    print(f'{area:.3f}')