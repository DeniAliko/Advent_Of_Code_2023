file = open("day2.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

# 12 red 13 green 14 blue

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# ['Game', '1:', '3', 'blue,', '4', 'red;', '1', 'red,', '2', 'green,', '6', 'blue;', '2', 'green']
dummy = 0
cache = {}
organizedInput = []
for line in inputFile:
    cache = {}
    splitLine = line.split()
    cache[int(splitLine[1][0:-1])] = "Game"
    
    values = []
    for i in range(2, len(splitLine) - 1):
        try:
            values.append([int(splitLine[i]), splitLine[i+1]])
        except ValueError:
            dummy += 1

    cache["vals"] = values
    organizedInput.append(cache)

for line in organizedInput:
    print(line)

redMax = 12
greenMax = 13
blueMax = 14
possible = []
for i in range(0, len(organizedInput)):
    possible.append(i+1)
for i in range(0, len(organizedInput)):
    gameDict = organizedInput[i]
    for value in gameDict["vals"]:
        # print(value)
        if value[1][0:4] == "blue":
            # print("blue")
            if value[0] > blueMax:
                # print(i+1)
                try:
                    possible.remove(i+1)
                except ValueError:
                    dummy += 1

        if value[1][0:3] == "red":
            if value[0] > redMax:
                # print(i+1)
                try:
                    possible.remove(i+1)
                except ValueError:
                    dummy += 1

        if value[1][0:5] == "green":
            if value[0] > greenMax:
                # print(i+1)
                try:
                    possible.remove(i+1)
                except ValueError:
                    dummy += 1

# print(possible)
print(sum(possible))

powers = []
for i in range(0, len(organizedInput)):
    minVals = [0, 0, 0]
    gameDict = organizedInput[i]
    for value in gameDict["vals"]:
        # print(value)
        if value[1][0:4] == "blue":
            if value[0] > minVals[0]:
                minVals[0] = value[0]

        if value[1][0:3] == "red":
            if value[0] > minVals[1]:
                minVals[1] = value[0]

        if value[1][0:5] == "green":
            if value[0] > minVals[2]:
                minVals[2] = value[0]

    power = 1
    for val in minVals:
        power *= val
    powers.append(power)

print(sum(powers))