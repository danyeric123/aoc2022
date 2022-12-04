import os
from typing import Tuple

path, _ = os.path.split(os.path.realpath(__file__))

with open(os.path.join(path, "input.txt")) as f:
    lines = [line.rstrip() for line in f]


def fully_contain(pair: Tuple[str, str]) -> bool:
    first1, first2 = [int(x) for x in pair[0].split("-")]
    second1, second2 = [int(x) for x in pair[1].split("-")]

    if (
        first1 <= second1 and first2 >= second2
    ) or (
        first1 >= second1 and first2 <= second2
    ):
        return True

    return False


sum_overlap = 0
for line in lines:
    pair = line.split(",")
    if fully_contain(pair):
        sum_overlap += 1

print(sum_overlap)


def overlap(pair: Tuple[str, str]) -> bool:
    first1, first2 = [int(x) for x in pair[0].split("-")]
    second1, second2 = [int(x) for x in pair[1].split("-")]

    if (
        first2 < second1 and first1 < second2
    ) or (
        first2 > second1 and first1 > second2
    ):
        return False

    return True


sum_overlap = 0
for line in lines:
    pair = line.split(",")
    if overlap(pair):
        sum_overlap += 1

print(sum_overlap)
