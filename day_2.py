import re

directions= []
quantities = []

horizontal = 0
depth = 0
aim = 0

with open("day-2.txt", "r") as input:
    directions_and_quantities = input.read()
    directions_and_quantities = re.split("\n|\s", directions_and_quantities)
    directions = directions_and_quantities[0::2]
    quantities = list(map(int, directions_and_quantities[1::2]))

for direction, quantity in zip(directions, quantities):
    match direction:
        case "forward":
            horizontal += quantity
            depth += aim * quantity
        case "down":
            aim += quantity
        case "up":
            aim -= quantity
        case _:
            print("unknown direction: ", direction)

print(horizontal * depth)