file = open("day18.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

import queue

directions = []
for line in inputFile:
    directions.append([line.split(" ")[0], int(line.split(" ")[1])])
    
# printList(directions)
pos = (0, 0)
visited = set({pos})
coordinates = [(0, 0)]

for line in directions:
    if line[0] == "U":
        for i in range(1, line[1] + 1):
            cachePos = (pos[0], pos[1] + 1)
            visited.add(cachePos)
            coordinates.append(cachePos)
            pos = cachePos

    elif line[0] == "D":
        for i in range(1, line[1] + 1):
            cachePos = (pos[0], pos[1] - 1)
            visited.add(cachePos)
            coordinates.append(cachePos)
            pos = cachePos

    elif line[0] == "R":
        for i in range(1, line[1] + 1):
            cachePos = (pos[0] + 1, pos[1])
            visited.add(cachePos)
            coordinates.append(cachePos)
            pos = cachePos

    elif line[0] == "L":
        for i in range(1, line[1] + 1):
            cachePos = (pos[0] - 1, pos[1])
            visited.add(cachePos)
            coordinates.append(cachePos)
            pos = cachePos

# print(visited)
# print(len(visited))

yMin = 999999
yMax = 0
xMin = 999999
xMax = 0
for coords in visited:
    if coords[0] > xMax:
        xMax = coords[0]
    if coords[0] < xMin:
        xMin = coords[0]
    if coords[1] > yMax:
        yMax = coords[1]
    if coords[1] < yMin:
        yMin = coords[1]

orgCoords = []
for i in range(yMin, yMax + 1):
    cacheList = []
    for coords in visited:
        if coords[1] == i:
            cacheList.append(coords)

    orgCoords.append(cacheList)
    cacheList = []

# printList(orgCoords)
orgerCoords = []
for x in orgCoords:
    cacheList = []
    for i in range(xMin, xMax + 1):
        for coords in x:
            if coords[0] == i:
                cacheList.append(coords)

    orgerCoords.append(cacheList)
            
# print(interior + len(visited))

vis = []
vis.append("." * (xMax - xMin + 3))
for y in range(yMin, yMax + 1):
    cacheString = "."
    for x in range(xMin, xMax + 1):
        found = False
        for coord in visited:
            if coord[1] == y and coord[0] == x:
                cacheString += "#"
                found = True
                break
        if not found:
            cacheString += "."
    cacheString += "."
    vis.append(cacheString)
vis.append("." * (xMax - xMin + 3))
# printList(vis)

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
currentChildren = []
nodeQueue.put([0,0])
while not nodeQueue.empty():
    focusNode = nodeQueue.get()
    if focusNode not in visited:
        visited.append(focusNode)
        for neighbor in getNeighbors(focusNode):
            if neighbor not in visited:
                nodeQueue.put(neighbor)

print(len(visited))
print((len(vis[0]) * len(vis))-len(visited))

# 34629 too low
# 41730 too high