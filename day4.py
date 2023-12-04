file = open("day4.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

score = 0
cards = []
for line in inputFile:
    first = line.split("|")[0].split(":")[1]
    last = line.split("|")[1]
    game = int(line.split("|")[0].split(":")[0].split()[1])

    firstNums = [int(x) for x in first.split()]
    lastNums = [int(x) for x in last.split()]

    count = 0
    for num in firstNums:
        if num in lastNums:
            count += 1

    cards.append([game, count])

# print(cards)
score = 0
for card in cards:
    if card[1] != 0:
        score += 2**(card[1]-1)

print(score)

# part 2
for card in cards:
    card.append(1)

for index in range(0, len(cards)):
    winning = cards[index][1]
    for i in range(1, winning + 1):
        cards[index + i][2] += cards[index][2]

score = 0
for card in cards:
    score += card[2]
print(score)