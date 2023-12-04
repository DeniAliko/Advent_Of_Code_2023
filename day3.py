file = open("day3.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

periodLine = "." * (len(inputFile[0]) + 2)
organizedInput = []
organizedInput.append(periodLine)
for line in inputFile:
    augLine = "." + line + "."
    organizedInput.append(augLine)
organizedInput.append(periodLine)

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

characters = ["", '=', '*', '+', '/', '&', '#', '-', '%', '$', '@']
print(characters)

nums = []
dummy = 0
for row in organizedInput:
    for i in range(0, len(row)):
        if row[i] in digits and row[i-1] not in digits:
            if row[i+1] in digits and row[i+2] in digits:
                nums.append(row[i]+row[i+1]+row[i+2])
                
            elif row[i+1] in digits:
                nums.append(row[i]+row[i+1])
                
            else:
                nums.append(row[i])

numCoords = {}
for i in range(0, len(organizedInput)):
    for j in range(0, len(organizedInput[i])):
        if organizedInput[i][j] in digits and organizedInput[i][j-1] not in digits:
            if organizedInput[i][j+1] in digits and organizedInput[i][j+2] in digits:
                numCoords[(j, i)] = organizedInput[i][j] + organizedInput[i][j+1] + organizedInput[i][j+2]
            elif organizedInput[i][j+1] in digits:
                numCoords[(j, i)] = organizedInput[i][j] + organizedInput[i][j+1]
            elif organizedInput[i][j] in digits:
                numCoords[(j, i)] = organizedInput[i][j]

parts = []
excluded = []

def charFind(num):
    basePos = []
    for coords in numCoords.keys():
        if numCoords[coords] == num:
            basePos.append(coords)
    for base in basePos:
        x = base[0]
        y = base[1]
        if len(num) == 2:
            check = [(x-1, y), 
                    (x-1, y-1), 
                    (x-1, y+1), 
                    (x, y-1), 
                    (x, y+1), 
                    (x+1, y-1), 
                    (x+1, y+1), 
                    (x+2, y-1), 
                    (x+2, y), 
                    (x+2, y+1)]
        elif len(num) == 3:
            check = [(x-1, y), 
                    (x-1, y-1), 
                    (x-1, y+1), 
                    (x, y-1), 
                    (x, y+1), 
                    (x+1, y-1), 
                    (x+1, y+1), 
                    (x+2, y-1),  
                    (x+2, y+1), 
                    (x+3, y-1), 
                    (x+3, y), 
                    (x+3, y+1)]
        elif len(num) == 1:
            check = [(x-1, y), 
                    (x-1, y-1), 
                    (x-1, y+1), 
                    (x, y-1), 
                    (x, y+1), 
                    (x+1, y-1), 
                    (x+1, y+1), 
                    (x+1, y)]
            
        found = False
        for coord in check:
            # print(organizedInput[coord[1]][coord[0]])
            if organizedInput[coord[1]][coord[0]] in characters:
                parts.append(num)
                found = True
                break
        
        if not found:
            excluded.append(num)

sum = 0
uniqueNums = []
for num in nums:
    if num not in uniqueNums:
        uniqueNums.append(num)
for num in uniqueNums:
    charFind(num)
# print(numCoords)
# for i in range(0, len(parts)-800):
#     print(parts[i])
newParts = []
for part in parts:
    if part not in newParts:
        newParts.append(part)
for part in parts:
    sum += int(part)
# print(len(parts))
print("sum", sum)
# 543852 TOO HIGH
# 65813 TOO LOW
# 389870 WRONG
# 251873 WRONG
# 539396 WRONG
# 305873 WRONG
# 531693 WRONG
# 328352 WRONG
# FINALLY 539433 RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH

# PART 2:

locations = {}
for num in uniqueNums:
    baseLocs = []
    for pos in numCoords.keys():
        if numCoords[pos] == num:
            baseLocs.append([pos[1], pos[0]])
    # print(baseLocs)
    for pos in baseLocs:
        if len(num) == 3:
            longPos = tuple([(pos[1], pos[1]+2), pos[0]])
            locations[longPos] = num
        elif len(num) == 2:
            longPos = tuple([(pos[1], pos[1]+1), pos[0]])
            locations[longPos] = num
        elif len(num) == 1:
            longPos = tuple([(pos[1], pos[1]+0), pos[0]])
            locations[longPos] = num

# print(locations)
products = []
def checkAround(tuple):
    x = tuple[0]
    y = tuple[1]
    u = (x, y+1)
    d = (x, y-1)
    l = (x-1, y)
    r = (x+1, y)
    ul = (x-1, y+1)
    ur = (x+1, y+1)
    dl = (x-1, y-1)
    dr = (x+1, y-1)
    dirs = [u, d, l, r, ul, ur, dl, dr]
    found = []

    for loc in locations.keys():
        for dir in dirs:
            if dir[1] == loc[1]:
                if dir[0] in range(loc[0][0], loc[0][1]+1):
                    found.append(locations[loc])

    uniqueFound = []
    for num in found:
        if num not in uniqueFound:
            uniqueFound.append(num)
    
    if len(uniqueFound) == 1:
        return
    product = 1
    for num in uniqueFound:
        product *= int(num)
    
    products.append(product)


for y in range(0, len(organizedInput)):
    for x in range(0, len(organizedInput[y])):
        current = organizedInput[y][x]
        if current == "*":
            checkAround((x, y))

# print(products)
sum = 0
for product in products:
    sum += product
print(sum)