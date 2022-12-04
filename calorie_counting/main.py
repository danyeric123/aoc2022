import os

path, _ = os.path.split(os.path.realpath(__file__))

with open(os.path.join(path, "input.txt")) as f:
    lines = [line.rstrip() for line in f]

calories = []
max_calorie = 0
for line in lines:
    if line == "":
        sum_of_elf = sum(calories)
        max_calorie = max(max_calorie, sum_of_elf)
        calories = []
    else:
        calories.append(int(line.rstrip()))

print(max_calorie)

calories = []
sums_of_calories = []
for line in lines:
    if line == "":
        sums_of_calories.append(sum(calories))
        calories = []
    else:
        calories.append(int(line.rstrip()))
sums_of_calories = sorted(sums_of_calories)
print(sums_of_calories[-1] + sums_of_calories[-2] + sums_of_calories[-3])
