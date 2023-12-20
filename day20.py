file = open("day20.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

def printList(list):
    for line in list:
        print(line)

modules = []
# xbroadcaster -> a, b, c
# broadcaster has the "x" tag
for line in inputFile:
    output = []
    modType = line[0]
    output.append(modType)
    modName = line.split(" -> ")[0][1:]
    output.append(modName)
    modRecievers = line.split(" -> ")[1].split(", ")
    output.append(modRecievers)
    output.append("low")
    modules.append(output)

printList(modules)
def send(moduleIn, signal):
    tag = moduleIn[0]
    name = moduleIn[1]
    targets = moduleIn[2]
    state = moduleIn[3]

    if tag == "x":
        for target in targets:
            for module in modules:
                if module[1] == target:
                    send(module, state)
    
    elif tag == "%":
        return
    # this problem is much worse than I thought lmao
    # conjunction modules SUUUUUUUUUUUUCK
            