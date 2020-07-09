input_steps = input()

steps_counter = 0

while input_steps != "Going home":
    steps_counter += int(input_steps)
    if steps_counter >= 10000:
        break
    input_steps = input()

if input_steps == "Going home":
    input_steps = input()
    steps_counter += int(input_steps)

if steps_counter >= 10000:
    print(f"Goal reached! Good job!\n{abs(10000 - int(steps_counter))} steps over the goal!")
else:
    print(f"{abs(10000 - int(steps_counter))} more steps to reach goal.")
