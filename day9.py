file = open("day9.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

organizedInput = []
for line in inputFile:
    organizedInput.append([int(x) for x in line.split()])

def findDiffs(list):
    output = []
    for i in range(1, len(list)):
        output.append(list[i] - list[i-1])

    return output

def extrapolate(list):
    if len(set(findDiffs(list))) == 1:
        return list[-1] + findDiffs(list)[-1]
    else:
        return list[-1] + extrapolate(findDiffs(list))
    
sum = 0
for line in organizedInput:
    sum += extrapolate(line)

print(sum)

def interpolate(list):
    if len(set(findDiffs(list))) == 1:
        return list[0] - findDiffs(list)[0]
    else:
        return list[0] - interpolate(findDiffs(list))

sum = 0
for line in organizedInput:
    sum += interpolate(line)

print(sum)