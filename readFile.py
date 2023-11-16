file = open("learnedPython.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))