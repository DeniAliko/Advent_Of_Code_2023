file = open("day11.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

expandedRows = []
for line in inputFile:
    expandedRows.append(line)
    if "#" not in line:
        expandedRows.append("." * len(line))

emptyCols = []
for i in range(0, len(expandedRows[0])):
    emptyTest = True
    for line in expandedRows:
        if line[i] == "#":
            emptyTest = False
    if emptyTest:
        emptyCols.append(i)

organizedInput = []
for line in expandedRows:
    cacheStr = ""
    for i in range(0, len(line)):
        cacheStr += line[i]
        if i in emptyCols:
            cacheStr += "."

    organizedInput.append(cacheStr)

# printList(organizedInput)
galaxies = []
for i in range(0, len(organizedInput)):
    for j in range(0, len(organizedInput[i])):
        if organizedInput[i][j] == "#":
            galaxies.append([j, i])

distances = []
for i in range(0, len(galaxies)):
    focus = galaxies[i]
    for j in range(i+1, len(galaxies)):
        partner = galaxies[j]
        distances.append(abs(partner[1] - focus[1]) + abs(partner[0] - focus[0]))

score = 0
for num in distances:
    score += num
print("p1:", score)

emptyRows = []
for i in range(0, len(inputFile)):
    if "#" not in inputFile[i]:
        emptyRows.append(i)

galaxies = []
for i in range(0, len(inputFile)):
    for j in range(0, len(inputFile[i])):
        if inputFile[i][j] == "#":
            galaxies.append([j, i])

distances = []
for i in range(0, len(galaxies)):
    focus = galaxies[i]
    for j in range(i+1, len(galaxies)):
        partner = galaxies[j]
        cacheDistance = [0, 0]
        if partner[1] > focus[1]:
            for i in range(focus[1], partner[1]):
                if i in emptyRows:
                    cacheDistance[1] += 1000000
                else:
                    cacheDistance[1] += 1
        elif partner[1] < focus[1]:
            for i in range(partner[1], focus[1]):
                if i in emptyRows:
                    cacheDistance[1] += 1000000
                else:
                    cacheDistance[1] += 1

        if partner[0] > focus[0]:
            for i in range(focus[0], partner[0]):
                if i in emptyCols:
                    cacheDistance[0] += 1000000
                else:
                    cacheDistance[0] += 1
        elif partner[0] < focus[0]:
            for i in range(partner[0], focus[0]):
                if i in emptyCols:
                    cacheDistance[0] += 1000000
                else:
                    cacheDistance[0] += 1

        distances.append(cacheDistance[0] + cacheDistance[1])

score = 0
for num in distances:
    score += num
print("p2:", score)