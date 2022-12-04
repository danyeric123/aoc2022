#!/usr/bin/env bash

mkdir $1
touch $1/input.txt
source .env

curl "https://adventofcode.com/2022/day/$2/input" \
  -H 'authority: adventofcode.com' \
  -H "cookie: ajs_user_id=$ajs_user_id; ajs_anonymous_id=$ajs_anonymous_id; session=$session;" \
  -H 'sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"' \
  --compressed >> $1/input.txt

touch $1/main.py
echo 'import os

path, _ = os.path.split(os.path.realpath(__file__))

with open(os.path.join(path, "input.txt")) as f:
    lines = [line.rstrip() for line in f]' >> $1/main.py
