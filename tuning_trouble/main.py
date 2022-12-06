import os

path, _ = os.path.split(os.path.realpath(__file__))

with open(os.path.join(path, "input.txt")) as f:
    line = f.readline()

for i in range(len(line)):
    if 4 == len(set(line[i:i+4])):
        print(i+4)
        break

for i in range(len(line)):
    if 14 == len(set(line[i:i+14])):
        print(i+14)
        break