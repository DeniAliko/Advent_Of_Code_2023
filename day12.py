file = open("day12.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

# ?###???????? 3,2,1
organizedInput = []
for line in inputFile:
    cacheList = [line.split(" ")[0]]
    for num in line.split(" ")[1].split(","):
        cacheList.append(int(num))

    organizedInput.append(cacheList)

def validCheck(rowList):
    row = rowList[0]
    groups = rowList[1:]
    
    hashTags = []
    cache = ""
    for char in row:
        if char == "#":
            cache += "#"
        elif char == "." and len(cache) != 0:
            hashTags.append(cache)
            cache = ""
    if cache != "":
        hashTags.append(cache)

    valid = True

    if len(groups) != len(hashTags):
        valid = False
    
    else:
        for i in range(0, len(groups)):
            if groups[i] != len(hashTags[i]):
                valid = False
                break

    return valid

print(validCheck(["..#...#...###.", 1, 1, 3]))
# print(validCheck(["#.#.###", 1,1,3]))

def stringify(list):
    output = ""
    for char in list:
        output += char

    return output

def allBinaries(length):
    output = []
    for i in range(0, (2**length)):
        binary = str(bin(i))[2:]
        cacheList = []
        for j in range(length - len(binary)):
            cacheList.append(0)
        for char in binary:
            cacheList.append(int(char))

        output.append(cacheList)

    # print(output)
    return output

def getPossible(rowList):
    row = [char for char in rowList[0]]

    output = []
    permutedRows = []

    permutations = allBinaries(row.count("?"))
    for permutation in permutations:
        bitIndex = 0
        cacheList = []
        for i in range(0, len(row)):
            if row[i] == "?":
                if permutation[bitIndex] == 1:
                    cacheList.append("#")
                else:
                    cacheList.append(".")
                bitIndex += 1
            else:
                cacheList.append(row[i])
        
        permutedRows.append(stringify(cacheList))

    for thingy in permutedRows:
        output.append([thingy] + rowList[1:])

    # printList(output)
    return(output)

validCount = 0
for line in organizedInput:
    print(line)
    print(organizedInput.index(line))
    for possibility in getPossible(line):
        if validCheck(possibility):
            validCount += 1

print(validCount)