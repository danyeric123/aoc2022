import os
from typing import List, Tuple

path, _ = os.path.split(os.path.realpath(__file__))

with open(os.path.join(path, "input.txt")) as f:
    lines = [line.rstrip() for line in f]


def get_compartments(comp: str) -> Tuple[str, str]:
    mid = len(comp) // 2
    return (comp[:mid], comp[mid:])


def items_shared(comp1: str, comp2: str) -> List[str]:
    shared = set()
    for item1, item2 in zip(comp1, comp2):
        if item1 in comp2:
            shared.add(item1)
        if item2 in comp1:
            shared.add(item2)

    return list(shared)


def get_proirity(char: str) -> int:
    ord_val = ord(char)
    if ord_val > 90:
        return ord_val - 96
    return ord_val - 38


sum_priorities = 0

for line in lines:
    comp1, comp2 = get_compartments(line)
    item_shared = items_shared(comp1, comp2)[0]
    sum_priorities += get_proirity(item_shared)

print(sum_priorities)


def item_shared_in_group(el1: str, el2: str, el3: str) -> str:
    shared = set()
    for item1, item2, item3 in zip(el1, el2, el3):
        if item1 in el2 and item1 in el3:
            shared.add(item1)
        if item2 in el1 and item2 in el3:
            shared.add(item2)
        if item3 in el1 and item3 in el2:
            shared.add(item3)

    return list(shared)[0]


sum_priorities = 0
for i in range(0, len(lines), 3):
    item = item_shared_in_group(lines[i], lines[i + 1], lines[i + 2])
    sum_priorities += get_proirity(item)

print(sum_priorities)
