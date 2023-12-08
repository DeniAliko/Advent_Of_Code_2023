import math
file = open("day8.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

instructions = "LRLRLRLRRLRRRLRLRLRRRLLRRLRRLRRLLRRLRRLRLRRRLRRLLRRLRRRLRRLRRRLRRRLLLRRLLRLLRRRLLRRLRLLRLLRRRLLRRLRRLRRRLRRLRLRRLRRLRLLRLRRRLRLRRLRLLRRLRRRLRRLRLRRLLLRRLRRRLRRRLRRLRRRLRLRRLRRLRRRLRRLRRLRRLRRLRRRLLRRRLLLRRRLRRLRRRLLRRRLRRLRRLLLLLRRRLRLRRLRRLLRRLRRLRLRLRRRLRRRLRRLLLRRRR"
# instructions = "LR"

elements = {}
for line in inputFile:
    start = line.split("=")[0][0:3]
    L = line.split("=")[1].split(",")[0][2:5]
    R = line.split("=")[1].split(",")[1][1:4]

    elements[start] = (L, R)
# print(elements)

current = "AAA"
count = 0
while current != "ZZZ":
    if instructions[(count)%len(instructions)] == "R":
        current = elements[current][1]
        count += 1
    elif instructions[(count)%len(instructions)] == "L":
        current = elements[current][0]
        count += 1
    if current == "ZZZ":
        break

print(count)

starts = []
ends = []
for thingy in elements.keys():
    if thingy[2] == "A":
        starts.append(thingy)
    elif thingy[2] == "Z":
        ends.append(thingy)

cycles = []
for start in starts:
    current = start
    count = 0
    while current not in ends:
        if instructions[(count)%len(instructions)] == "R":
            current = elements[current][1]
            count += 1
        elif instructions[(count)%len(instructions)] == "L":
            current = elements[current][0]
            count += 1
        if current in ends:
            # print(count)
            cycles.append(count)
            break

print(math.lcm(cycles[0], cycles[1], cycles[2], cycles[3], cycles[4], cycles[5]))