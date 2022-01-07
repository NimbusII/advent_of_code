import os
import math

measurements = []

with open("day-1.txt", "r") as input:
    measurements = input.read().split("\n")
    measurements = list(map(int, measurements))

windows = zip(measurements[0:-2], measurements[1:-1], measurements[2:])

previous = math.inf
increase_count = 0

for window in list(windows):

    if sum(window) > previous:
        increase_count += 1

    previous = sum(window)

print(increase_count)