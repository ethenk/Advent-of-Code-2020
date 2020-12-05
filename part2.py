import re

file = open("/Users/kisne/Documents/Development/Advent of Code 2020/1/data.txt", 'r')

for value in file:
    # print("Line: " + value)
    file2 = open("/Users/kisne/Documents/Development/Advent of Code 2020/1/data.txt", 'r')

    for value2 in file2:
        # print("Line: " + value)
        file3 = open("/Users/kisne/Documents/Development/Advent of Code 2020/1/data.txt", 'r')
    
        for value3 in file3:
            # print("Line 2: " + value2)
            lineTotal = int(value) + int(value2) + int(value3)
            # print("Line total: " + str(lineTotal))

            if (lineTotal == 2020):
                lineMultiply = int(value) * int(value2) * int(value3)
                print("Value 1: " + value)
                print("Value 2: " + value2)
                print("Value 3: " + value3)
                print("Answer: " + str(lineMultiply))
            else:
                # print("Answer not found\n")
                pass