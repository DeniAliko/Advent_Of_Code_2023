file = open("day16.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

import queue

# printList(inputFile)

# /
fSlash = []
# \
bSlash = []
# -
hSplit = []
# |
vSplit = []

for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        if inputFile[i][j] == "/":
            fSlash.append([j, i])
        elif inputFile[i][j] == "\\":
            bSlash.append([j, i])
        elif inputFile[i][j] == "|":
            vSplit.append([j, i])
        elif inputFile[i][j] == "-":
            hSplit.append([j, i])

beams = [[[0, 0], "R"]]

def move(beam):
    coords = beam[0]
    direction = beam[1]

    if direction == "U":
        if coords[1] == 0:
            return
        else:
            if [coords[0], coords[1] - 1] in fSlash:
                coords[1] -= 1
                direction = "R"
            elif [coords[0], coords[1] - 1] in bSlash:
                coords[1] -= 1
                direction = "L"
            elif [coords[0], coords[1] - 1] in vSplit:
                coords[1] -= 1
            elif [coords[0], coords[1] - 1] in hSplit:
                coords[1] -= 1
                direction = "R"
                beams.append([coords.copy(), "L"])

    elif direction == "D":
        if coords[1] == len(inputFile) - 1:
            return
        else:
            if [coords[0], coords[1] + 1] in fSlash:
                coords[1] += 1
                direction = "L"
            elif [coords[0], coords[1] + 1] in bSlash:
                coords[1] += 1
                direction = "R"
            elif [coords[0], coords[1] + 1] in vSplit:
                coords[1] += 1
            elif [coords[0], coords[1] + 1] in hSplit:
                coords[1] += 1
                direction = "L"
                beams.append([coords.copy(), "R"])

    elif direction == "R":
        if coords[0] == len(inputFile[0]) - 1:
            return
        else:
            if [coords[0] + 1, coords[1]] in fSlash:
                coords[0] += 1
                direction = "U"
            elif [coords[0] + 1, coords[1]] in bSlash:
                coords[0] += 1
                direction = "D"
            elif [coords[0] + 1, coords[1]] in hSplit:
                coords[0] += 1
            elif [coords[0] + 1, coords[1]] in vSplit:
                coords[0] += 1
                direction = "U"
                beams.append([coords.copy(), "D"])

    elif direction == "L":
        if coords[0] == 0:
            return
        else:
            if [coords[0] - 1, coords[1]] in fSlash:
                coords[0] -= 1
                direction = "D"
            elif [coords[0] - 1, coords[1]] in bSlash:
                coords[0] -= 1
                direction = "U"
            elif [coords[0] - 1, coords[1]] in hSplit:
                coords[0] -= 1
            elif [coords[0] - 1, coords[1]] in vSplit:
                coords[0] -= 1
                direction = "D"
                beams.append([coords.copy(), "U"])

visited = set()
while True:
    for beam in beams:
        visited.add(tuple(beam[0]))
        print(len(visited))
        print(visited)
        move(beam)