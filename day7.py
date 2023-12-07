file = open("day7.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

cardsBids = {}
interimOrg = []
for line in inputFile:
    interimOrg.append(line.split()[0])
    cardsBids[line.split()[0]] = int(line.split()[1])

# Confirm correct bids for each hand:
# for line in inputFile:
#     if int(line.split()[1]) != int(cardsBids[line.split()[0]]):
#         print("actual:", line)
#         print("got:", cardsBids[line.split()[0]])

alphabet = "23456789TJQKA"
organizedInput = sorted(interimOrg, key=lambda word: [alphabet.index(c) for c in word])
# print(organizedInput)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
quint = []
quads = []
boats = []
trips = []
twoPair = []
pair = []
highCard = []

# organize the hands
for line in organizedInput:
    hand = [x for x in line]
    if len(set(hand)) == 1:
        quint.append(line)
    elif len(set(hand)) == 2:
        quad = False
        for card in cards:
            if hand.count(card) == 4:
                quad = True
                quads.append(line)
        if not quad:
            boats.append(line)
    elif len(set(hand)) == 3:
        trip = False
        for card in cards:
            if hand.count(card) == 3:
                trip = True
                trips.append(line)
        if not trip:
            twoPair.append(line)
    elif len(set(hand)) == 4:
        pair.append(line)
    elif len(set(hand)) == 5:
        highCard.append(line)

for line in organizedInput:
    if line not in quint and line not in quads and line not in boats and line not in trips and line not in twoPair and line not in pair:
        highCard.append(line)

# def orderList(list):
#     output = []
#     for card in cards:
#         # 1st digit
#         cacheList = []
#         for thingy in list:
#             hand = [x for x in thingy[0]]
#             if hand[0] == card:
#                 cacheList.append(hand)

#         if len(cacheList) == 1:
#             output.append(cacheList[0])
#         elif len(cacheList) > 1:
#             orderedSubset = orderList([x[1:] for x in cacheList])

#             for subset in orderedSubset:
#                 for hand in list:
#                     if hand[0][1:] == subset:
#                         output.append([x for x in hand[0]])
#                         # figure out what's happening with the recursion

#     realOutput = []
#     for hand in output:
#         cacheStr = ""
#         for char in hand:
#             cacheStr += char

#         for hand in list:
#             if hand[0] == cacheStr:
#                 realOutput.append(hand)

#     return realOutput

def orderList(list):
    alphabet = "23456789TJQKA"
    hands = [x[0] for x in list]
    sortedHands = sorted(hands, key=lambda word: [alphabet.index(c) for c in word])
    output = []
    for hand in sortedHands:
        for item in list:
            if item[0] == hand:
                output.append(item)

    return output

# print("high card", highCard)
# print("pair", pair)
# print("two pair", twoPair)
# print("trips", trips)
# print("boats", boats)
# print("quads", quads)
# print("quint", quint)

fullOrder = []
for hand in highCard:
    fullOrder.append(hand)
for hand in pair:
    fullOrder.append(hand)
for hand in twoPair:
    fullOrder.append(hand)
for hand in trips:
    fullOrder.append(hand)
for hand in boats:
    fullOrder.append(hand)
for hand in quads:
    fullOrder.append(hand)
for hand in quint:
    fullOrder.append(hand)

# print(fullOrder)
score = 0
for i in range(0, len(fullOrder)):
    score += (i + 1) * cardsBids[fullOrder[i]]


# for card in fullOrder:
#     print(card)

print("score:", score)


# PART 2:

quint = []
quads = []
boats = []
trips = []
twoPair = []
pair = []
highCard = []

alphabet = "J23456789TQKA"
organizedInput = sorted(interimOrg, key=lambda word: [alphabet.index(c) for c in word])
# print(organizedInput)

for line in organizedInput:
    hand = [x for x in line]

    if "J" not in hand:
        if len(set(hand)) == 1:
            quint.append(line)
        elif len(set(hand)) == 2:
            quad = False
            for card in cards:
                if hand.count(card) == 4:
                    quad = True
                    quads.append(line)
            if not quad:
                boats.append(line)
        elif len(set(hand)) == 3:
            trip = False
            for card in cards:
                if hand.count(card) == 3:
                    trip = True
                    trips.append(line)
            if not trip:
                twoPair.append(line)
        elif len(set(hand)) == 4:
            pair.append(line)
        elif len(set(hand)) == 5:
            highCard.append(line)

    else:
        if len(set(hand)) == 1:
            quint.append(line)
        elif len(set(hand)) == 2:
            quint.append(line)
        elif len(set(hand)) == 3:
            if hand.count("J") == 1:
                quad = False
                for card in cards:
                    if hand.count(card) == 3:
                        quads.append(line)
                        quad = True
                        break
                if not quad:
                    boats.append(line)
            elif hand.count("J") == 2:
                quads.append(line)
            elif hand.count("J") == 3:
                quads.append(line)
        elif len(set(hand)) == 4:
            trips.append(line)
        elif len(set(hand)) == 5:
            pair.append(line)

fullOrder = []
for hand in highCard:
    fullOrder.append(hand)
for hand in pair:
    fullOrder.append(hand)
for hand in twoPair:
    fullOrder.append(hand)
for hand in trips:
    fullOrder.append(hand)
for hand in boats:
    fullOrder.append(hand)
for hand in quads:
    fullOrder.append(hand)
for hand in quint:
    fullOrder.append(hand)

# print(fullOrder)
score = 0
for i in range(0, len(fullOrder)):
    score += (i + 1) * cardsBids[fullOrder[i]]

# print("high card", highCard)
# print("pair", pair)
# print("two pair", twoPair)
# print("trips", trips)
# print("boats", boats)
# print("quads", quads)
# print("quint", quint)

print("P2:", score)
# 250045235 too high