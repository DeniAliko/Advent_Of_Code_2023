file = open("day10.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

coords = {}
for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        coords[(j, i)] = inputFile[i][j]

for point in coords.keys():
    if coords[point] == "S":
        start = point

current = [start[0], start[1] + 1]
print(current)
global direction
direction = "S"
pipeCount = 0

def walk():
    global direction
    global pipeCount
    currentPipe = coords[tuple(current)]

    if currentPipe == "|":
        if direction == "S":
            current[1] += 1 
        elif direction == "N":
            current[1] -= 1 
    elif currentPipe == "-":
        if direction == "E":
            current[0] += 1 
        elif direction == "W":
            current[0] -= 1 
    elif currentPipe == "F":
        if direction == "N":
            direction = "E"
            current[0] += 1
        elif direction == "W":
            direction = "S"
            current[1] += 1
    elif currentPipe == "7":
        if direction == "N":
            direction = "W"
            current[0] -= 1
        elif direction == "E":
            direction = "S"
            current[1] += 1
    elif currentPipe == "L":
        if direction == "S":
            direction = "E"
            current[0] += 1
        elif direction == "W":
            direction = "N"
            current[1] -= 1
    elif currentPipe == "J":
        if direction == "S":
            direction = "W"
            current[0] -= 1
        elif direction == "E":
            direction = "N"
            current[1] -= 1

    if currentPipe != ".":
        pipeCount += 1
    return

pipePartCoords = []

while coords[tuple(current)] != "S":
# for i in range(20):
    walk()
    pipePartCoords.append(current)
    # print(current)
    # print(direction)

# print(pipeCount)
print("P1:", (pipeCount + 1)/2)

print(pipePartCoords)