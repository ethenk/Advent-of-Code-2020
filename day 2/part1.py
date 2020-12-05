import re

file = open("/Users/kisne/Documents/Development/Advent of Code 2020/day 2/data.txt", 'r')

for value in file:
    min = value.split("-")[0]
    max = value.split(" ")[0].lstrip("-")[-1]
    print(max)
    