file = open("day14.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

rollerCoords = []
blockCoords = [[i, -1] for i in range(0, len(inputFile[0]))]
for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        if inputFile[i][j] == "#":
            blockCoords.append([j, i])
        elif inputFile[i][j] == "O":
            rollerCoords.append([j, i])

class Boulder:
    def __init__(self, coords, isStuck):
        self.coords = coords
        self.isStuck = isStuck

    def move(self):
        if not self.isStuck:
            if [self.coords[0], self.coords[1]-1] not in blockCoords:
                self.coords[1] -= 1
                # print(self.coords)
            elif [self.coords[0], self.coords[1]-1] in blockCoords:
                self.isStuck = True
                blockCoords.append(rollers[i].coords)

rollers = []
for coords in rollerCoords:
    rollers.append(Boulder(coords, False))

allStuck = [False for i in rollers]
while False in allStuck:
    for i in range(0, len(rollers)):
        if rollers[i].isStuck == True:
            allStuck[i] = True
        elif rollers[i].isStuck == False:
            rollers[i].move()

sum = 0
for roller in rollers:
    sum += len(inputFile) - roller.coords[1]

print(sum)

