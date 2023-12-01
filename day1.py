file = open("day1.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

# print(inputFile)

def getF(x):
    for char in x:
        try:
            return int(char)
        except ValueError:
            continue
            

def getL(x):
    for i in range(len(x) - 1, -1, -1):
        try:
            return int(x[i])
        except ValueError:
            continue

values = []
for line in inputFile:
    values.append(str(getF(line)) + str(getL(line)))

newVals = []
for value in values:
    newVals.append(int(value))

print(sum(newVals))

# part 2:

words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
# print(words.keys())
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# def left(x):
#     for i in range(0, len(x)):
#         if x[i] in digits:
#             if x[i] in words.keys():
#                 return words[x[i]]
#             else:
#                 return x[i]
            
# def right(x):
#     for i in range(len(x) - 1, -1, -1):
#         if x[i] in digits:
#             if x[i] in words.keys():
#                 return words[x[i]]
#             else:
#                 return x[i]

test = ["two1nine", 
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]
values = []    

testRepeat = ["eighteight9dnvcqznjvfpreight"]

for line in inputFile:
    Fpositions = {}
    for digit in digits:
        if line.find(digit) != -1:
            Fpositions[digit] = line.find(digit)
    minIndex = min(Fpositions.values())
    minVal = ""
    for key in Fpositions.keys():
        if Fpositions[key] == minIndex:
            minVal = key
    newMin = ""
    if minVal in words.keys():
        newMin = words[minVal]
    else:
        newMin = minVal

    Lpositions = {}
    for digit in digits:
        if line.rfind(digit) != -1:
            Lpositions[digit] = line.rfind(digit)
    maxIndex = max(Lpositions.values())
    maxVal = ""
    for key in Lpositions.keys():
        if Lpositions[key] == maxIndex:
            maxVal = key
    newMax = ""
    if maxVal in words.keys():
        newMax = words[maxVal]
    else:
        newMax = maxVal

    values.append(newMin + newMax)

print(values)

newVals = []
for value in values:
    newVals.append(int(value))

print(sum(newVals))