file = open("day15.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

strInput = inputFile[0].split(",")
# printList(strInput)

values = []
for hash in strInput:
    currentValue = 0
    for char in hash:
        currentValue += int(ord(char))
        currentValue *= 17
        currentValue = currentValue % 256
    values.append(currentValue)

print(sum(values))

def hashify(string):
    currentValue = 0
    for char in string:
        currentValue += int(ord(char))
        currentValue *= 17
        currentValue = currentValue % 256

    return currentValue

boxes = []
for i in range(256):
    boxes.append([])

for step in strInput:
    if "=" in step:
        label = step.split("=")[0]
        focal = step.split("=")[1]
        boxIndex = hashify(label)

        if label not in [x[0] for x in boxes[boxIndex]]:
            boxes[boxIndex].append([label, focal])
        else:
            for i in range(0, len(boxes[boxIndex])):
                if boxes[boxIndex][i][0] == label:
                    boxes[boxIndex][i][1] = focal
                    break

    elif "-" in step:
        label = step.split("-")[0]
        boxIndex = hashify(label)
        for i in range(0, len(boxes[boxIndex])):
            if boxes[boxIndex][i][0] == label:
                boxes[boxIndex].pop(i)
                break

boxSum = 0
for i in range(0, len(boxes)):
    for j in range(0, len(boxes[i])):
        boxSum += (i+1)*(j+1)*(int(boxes[i][j][1]))

print(boxSum)