file = open("day10.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

import queue

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

    pipePartCoords.append(tuple(current))

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
    # print(current)
    # print(direction)

# print(pipeCount)
print("P1:", (pipeCount + 1)/2)

# interior = []
# passedPipeCount = 0
# for y in range(0, len(inputFile)):
#     passedPipeCount = 0

#     rowPipeCount = 0
#     for x in range(0, len(inputFile[y])):
#         if (x, y) in pipePartCoords:
#             rowPipeCount += 1

#     for x in range(0, len(inputFile[y])):
#         if (x,y) in pipePartCoords:
#             passedPipeCount += 1
#             continue

#         if rowPipeCount % 2 == 0 and passedPipeCount > 0 and passedPipeCount < rowPipeCount:
#             if passedPipeCount % 2 == 1 and (rowPipeCount - passedPipeCount) % 2 == 1:
#                 interior.append((x, y))

#         elif rowPipeCount % 2 == 1 and passedPipeCount > 0 and passedPipeCount < rowPipeCount:
#             if passedPipeCount % 2 == 1 or (rowPipeCount - passedPipeCount) % 2 == 1:
#                 interior.append((x, y))

# printList(interior)
# print(len(interior))

vis = []
for i in range(0, len(inputFile)):
    line = inputFile[i]
    cache1 = ""
    cache2 = ""
    cache3 = ""
    for j in range(0, len(line)):
        char = line[j]
        if (j, i) in pipePartCoords:
            if char == "|":
                cache1 += ".#."
                cache2 += ".#."
                cache3 += ".#."
            elif char == "-":
                cache1 += "..."
                cache2 += "###"
                cache3 += "..."
            elif char == "J":
                cache1 += ".#."
                cache2 += "##."
                cache3 += "..."
            elif char == "F":
                cache1 += "..."
                cache2 += ".##"
                cache3 += ".#."
            elif char == "L":
                cache1 += ".#."
                cache2 += ".##"
                cache3 += "..."
            elif char == "7":
                cache1 += "..."
                cache2 += "##."
                cache3 += ".#."
        elif char == "S":
            cache1 += ".#."
            cache2 += ".#."
            cache3 += ".#."
        else:
            cache1 += "..."
            cache2 += "..."
            cache3 += "..."

    vis.append(cache1)
    vis.append(cache2)
    vis.append(cache3)

# printList(vis)

def getSquare(tuple):
    x = tuple[0]
    y = tuple[1]
    output = []

    output.append(vis[y-1][x])
    output.append(vis[y+1][x])
    output.append(vis[y][x-1])
    output.append(vis[y][x+1])
    output.append(vis[y-1][x-1])
    output.append(vis[y-1][x+1])
    output.append(vis[y+1][x-1])
    output.append(vis[y+1][x+1])

    return output

def getNeighbors(tuple):
    x = tuple[0]
    y = tuple[1]
    output = []

    if x >= 1:
        if vis[y][x-1] == ".":
            output.append([x-1, y])
    if x <= len(vis[0]) - 2:
        if vis[y][x+1] == ".":
            output.append([x+1, y])
    if y >= 1:
        if vis[y-1][x] == ".":
            output.append([x, y-1])
    if y <= len(vis) - 2:
        if vis[y+1][x] == ".":
            output.append([x, y+1])
    if y >= 1 and x >= 1:
        if vis[y-1][x-1] == ".":
            output.append([x-1, y-1])
    if y <= len(vis) - 2 and x >= 1:
        if vis[y+1][x-1] == ".":
            output.append([x-1, y+1])
    if y >= 1 and x <= len(vis[0]) - 2:
        if vis[y-1][x+1] == ".":
            output.append([x+1, y-1])
    if y <= len(vis) - 2 and x <= len(vis[0]) - 2:
        if vis[y+1][x+1] == ".":
            output.append([x+1, y+1])

    return output

nodeQueue = queue.Queue()
visited = []
prevNode = start
currentChildren = []
nodeQueue.put([0,0])
while not nodeQueue.empty():
    focusNode = nodeQueue.get()
    if focusNode not in visited:
        visited.append(focusNode)
        for neighbor in getNeighbors(focusNode):
            if neighbor not in visited:
                nodeQueue.put(neighbor)

# printList(visited)

insideCount = 0
for y in range(1, len(vis), 3):
    for x in range(1, len(vis[y]), 3):
        if (int((x-1)/3), int((y-1)/3)) not in pipePartCoords:
            neighbors = getNeighbors((x, y))
            outside = False
            for neighbor in neighbors:
                if neighbor in visited:
                    outside = True
                    break

            if not outside:
                insideCount += 1

print(insideCount)