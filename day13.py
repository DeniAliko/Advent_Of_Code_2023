file = open("day13.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

organizedInput = []
cacheList = []
for i in range(0, len(inputFile)):
    line = inputFile[i]
    if line != "":
        cacheList.append(line)
    elif line == "":
        organizedInput.append(cacheList)
        cacheList = []
organizedInput.append(cacheList)

# printList(organizedInput)

rowSum = 0
for array in organizedInput:
    for i in range(1, len(array)):
        # The idea here is to check from a border of the rectangle to the i-index
        isMirrorRow = True
        if i <= len(array) / 2:
            for diff in range(0, i):
                if array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False

        elif i > len(array) / 2:
            for diff in range(0, len(array) - i):
                if array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False

        if isMirrorRow:
            rowSum += i
            break

# print(rowSum)
def columnify(list):
    output = []
    cache = []
    for i in range(0, len(list[0])):
        for j in range(0, len(list)):
            cache.append(list[j][i])
        output.append(cache)
        cache = []

    return output

columnOrg = []
for array in organizedInput:
    columnOrg.append(columnify(array))

colSum = 0
for array in columnOrg:
    for i in range(1, len(array)):
        # The idea here is to check from a border of the rectangle to the i-index
        isMirrorRow = True
        if i <= len(array) / 2:
            for diff in range(0, i):
                if array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False

        elif i > len(array) / 2:
            for diff in range(0, len(array) - i):
                if array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False

        if isMirrorRow:
            colSum += i
            break

# print(colSum)

print("p1:", colSum + 100*rowSum)

def isClose(list1, list2):
    discrepancies = 0
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            discrepancies += 1

    if discrepancies == 1:
        return True
    else:
        return False
    
rowSum = 0
for array in organizedInput:
    for i in range(1, len(array)):
        # The idea here is to check from a border of the rectangle to the i-index
        isMirrorRow = True
        smudgeFound = 0
        if i <= len(array) / 2:
            for diff in range(0, i):
                if not isClose(array[i-diff-1], array[i+diff]) and array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False
                else:
                    if isClose(array[i-diff-1], array[i+diff]):
                        smudgeFound += 1

        elif i > len(array) / 2:
            for diff in range(0, len(array) - i):
                if not isClose(array[i-diff-1], array[i+diff]) and array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False
                else:
                    if isClose(array[i-diff-1], array[i+diff]):
                        smudgeFound += 1

        if isMirrorRow and smudgeFound == 1:
            rowSum += i
            break

print(rowSum)

colSum = 0
for array in columnOrg:
    for i in range(1, len(array)):
        # The idea here is to check from a border of the rectangle to the i-index
        isMirrorRow = True
        smudgeFound = 0
        if i <= len(array) / 2:
            for diff in range(0, i):
                if not isClose(array[i-diff-1], array[i+diff]) and array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False
                else:
                    if isClose(array[i-diff-1], array[i+diff]):
                        smudgeFound += 1

        elif i > len(array) / 2:
            for diff in range(0, len(array) - i):
                if not isClose(array[i-diff-1], array[i+diff]) and array[i-diff-1] != array[i+diff]:
                    isMirrorRow = False
                else:
                    if isClose(array[i-diff-1], array[i+diff]):
                        smudgeFound += 1

        if isMirrorRow and smudgeFound == 1:
            colSum += i
            break

print(colSum)

print(colSum + 100*rowSum)