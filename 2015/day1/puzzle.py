import os

with open("input.txt", "r") as file:
    data = file.read()

floor = 0
for c in data:
    if c == "(":
        floor += 1
    else:
        floor -= 1

print(floor)