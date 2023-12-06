races = [[55, 246], [82, 1441], [64, 1012], [90, 1111]]
# races = [[7, 9], [15, 40], [30, 200]]

counts = []
for race in races:
    count = 0
    for held in range(0, race[0]):
        distance = (race[0]-held) * held
        if distance > race[1]:
            count += 1

    counts.append(count)

product = 1
for count in counts:
    product *= count
print(product)

bigRace = [55826490, 246144110121111]
# bigRace = [71530, 940200]

count = 0
bottom = 0
for held in range(0, bigRace[0]):
    distance = (bigRace[0]-held) * held
    if distance > bigRace[1]:
        bottom = held
        break

top = 0
for held in range(bigRace[0], 0, -1):
    distance = (bigRace[0]-held) * held
    if distance > bigRace[1]:
        top = held
        break

print(1 + top - bottom)
# 46173808 too low