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

printList(organizedInput)