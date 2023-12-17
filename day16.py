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

beams = queue.Queue()

class Beam:
    def __init__(self, coords, direction, stop):
        self.coords = coords
        self.direction = direction
        self.stop = stop

    def move(self):
        if not self.stop:
            if self.direction == "N":
                if self.coords[1] - 1 < 0:
                    self.stop = True
                    return
                elif [self.coords[0], self.coords[1]-1] in fSlash:
                    self.coords[1] -= 1
                    self.direction = "E"
                elif [self.coords[0], self.coords[1]-1] in bSlash:
                    self.coords[1] -= 1
                    self.direction = "W"
                elif [self.coords[0], self.coords[1]-1] in vSplit:
                    self.coords[1] -= 1
                elif [self.coords[0], self.coords[1]-1] in hSplit:
                    self.coords[1] -= 1
                    self.direction = "E"
                    beams.put(Beam(self.coords, "W", False))
                else:
                    self.coords[1] -= 1

            elif self.direction == "S":
                if self.coords[1] + 1 >= len(inputFile):
                    self.stop = True
                    return
                elif [self.coords[0], self.coords[1]+1] in fSlash:
                    self.coords[1] += 1
                    self.direction = "W"
                elif [self.coords[0], self.coords[1]+1] in bSlash:
                    self.coords[1] += 1
                    self.direction = "E"
                elif [self.coords[0], self.coords[1]+1] in vSplit:
                    self.coords[1] += 1
                elif [self.coords[0], self.coords[1]+1] in hSplit:
                    self.coords[1] += 1
                    self.direction = "W"
                    beams.put(Beam(self.coords, "E", False))
                else:
                    self.coords[1] += 1
                
            elif self.direction == "E":
                if self.coords[0] + 1 >= len(inputFile[0]):
                    self.stop = True
                    return
                elif [self.coords[0] + 1, self.coords[1]] in fSlash:
                    self.coords[0] += 1
                    self.direction = "N"
                elif [self.coords[0] + 1, self.coords[1]] in bSlash:
                    self.coords[0] += 1
                    self.direction = "S"
                elif [self.coords[0] + 1, self.coords[1]] in vSplit:
                    self.coords[0] += 1
                    self.direction = "N"
                    beams.put(Beam(self.coords, "S", False))
                elif [self.coords[0] + 1, self.coords[1]] in hSplit:
                    self.coords[0] += 1
                else:
                    self.coords[0] += 1

            elif self.direction == "W":
                if self.coords[0] - 1 < 0:
                    self.stop = True
                    return
                elif [self.coords[0] - 1, self.coords[1]] in fSlash:
                    self.coords[0] -= 1
                    self.direction = "S"
                elif [self.coords[0] - 1, self.coords[1]] in bSlash:
                    self.coords[0] -= 1
                    self.direction = "N"
                elif [self.coords[0] - 1, self.coords[1]] in vSplit:
                    self.coords[0] -= 1
                    self.direction = "S"
                    beams.put(Beam(self.coords, "N", False))
                elif [self.coords[0] - 1, self.coords[1]] in hSplit:
                    self.coords[0] -= 1
                else:
                    self.coords[0] -= 1

beams.put(Beam([0, 0], "E", False))
visited = set({(0, 0)})

while not beams.empty():
    focusBeam = beams.get()
    while not focusBeam.stop:
        focusBeam.move()
        # print(focusBeam.coords)
        visited.add((focusBeam.coords[0], focusBeam.coords[1]))

    # print(len(visited))
    vis = ["x0123456789"]
    for i in range(0, len(inputFile)):
        cacheString = str(i)
        for j in range(0, len(inputFile[i])):
            if (j, i) in visited:
                cacheString += "#"
            else:
                cacheString += "."
        vis.append(cacheString)

    printList(vis)

# 2333 too low
# 2394 too low
# 2510 too low
# not 2588
vis = ["x0123456789"]
for i in range(0, len(inputFile)):
    cacheString = str(i)
    for j in range(0, len(inputFile[i])):
        if (j, i) in visited:
            cacheString += "#"
        else:
            cacheString += "."
    vis.append(cacheString)

printList(vis)
print(len(visited))