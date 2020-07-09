width = int(input())
height = int(input())

cake_piece = width * height

while cake_piece > 0:
    line = input()
    if line == "STOP":
        print(f"{cake_piece} pieces are left.")
        break

    current_pieces = int(line)
    cake_piece -= current_pieces

if cake_piece <= 0:
    print(f"No more cake left! You need {abs(cake_piece)} pieces more.")