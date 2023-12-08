file = open("day8.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

instructions = "LRLRLRLRRLRRRLRLRLRRRLLRRLRRLRRLLRRLRRLRLRRRLRRLLRRLRRRLRRLRRRLRRRLLLRRLLRLLRRRLLRRLRLLRLLRRRLLRRLRRLRRRLRRLRLRRLRRLRLLRLRRRLRLRRLRLLRRLRRRLRRLRLRRLLLRRLRRRLRRRLRRLRRRLRLRRLRRLRRRLRRLRRLRRLRRLRRRLLRRRLLLRRRLRRLRRRLLRRRLRRLRRLLLLLRRRLRLRRLRRLLRRLRRLRLRLRRRLRRRLRRLLLRRRR"
instructions = "LR"

elements = {}
for line in inputFile:
    start = line.split("=")[0][0:3]
    L = line.split("=")[1].split(",")[0][2:5]
    R = line.split("=")[1].split(",")[1][1:4]

    elements[start] = (L, R)
print(elements)

# current = "AAA"
# count = 0
# while current != "ZZZ":
#     if instructions[(count)%len(instructions)] == "R":
#         current = elements[current][1]
#         count += 1
#     elif instructions[(count)%len(instructions)] == "L":
#         current = elements[current][0]
#         count += 1
#     if current == "ZZZ":
#         print(count)
#         break


# current1 = "LCA"
# current2 = "NVA"
# current3 = "GCA"
# current4 = "SXA"
# current5 = "AAA"
# current6 = "GMA"
current1 = "11A"
current2 = "22A"
count = 0
done = False
while not done:
    if instructions[(count)%len(instructions)] == "R":
        current1 = elements[current1][1]
        current2 = elements[current1][1]
        # current3 = elements[current1][1]
        # current4 = elements[current1][1]
        # current5 = elements[current1][1]
        # current6 = elements[current1][1]
        count += 1
    elif instructions[(count)%len(instructions)] == "L":
        current1 = elements[current1][0]
        current2 = elements[current1][0]
        # current3 = elements[current1][0]
        # current4 = elements[current1][0]
        # current5 = elements[current1][0]
        # current6 = elements[current1][0]
        count += 1
    if current1[2] == "Z" and current2[2] == "Z":
        #  and current3[2] == "Z" and current4[2] == "Z" and current5[2] == "Z" and current6[2] == "Z"
        done = True
    print(count)
    print("Path1:", current1)
    print("Path2:", current2)