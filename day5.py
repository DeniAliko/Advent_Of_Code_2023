file = open("day5.txt")
inputFile = []
linesInFile = file.readlines()
for i in linesInFile:
    inputFile.append(format(i.strip()))

starts = [int(x) for x in inputFile[0].split()[1:len(inputFile)]]
seedSoil = []
soilFert = []
fertWater = []
waterLight = []
lightTemp = []
tempHumid = []
humidLoc = []
maps = [seedSoil, soilFert, fertWater, waterLight, lightTemp, tempHumid, humidLoc]
currentMapIndex = -1
for line in inputFile:
    if line.split(" ")[0] == "seeds:":
        continue
    if line in ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]:
        currentMapIndex += 1
        continue
    if line == "":
        continue
    maps[currentMapIndex].append([int(x) for x in line.split()])

# print(maps)
locations = []
print(starts)
for seed in starts:
    for map in maps[0]:
        if seed >= map[1] and seed <= map[1] + map[2] - 1:
            soil = map[0] + (seed - map[1])
            found = True
    if not found:
        soil = seed
    # print(soil)
    found = False

    for map in maps[1]:
        if soil >= map[1] and soil <= map[1] + map[2] - 1:
            fert = map[0] + (soil - map[1])
            found = True
    if not found:
        fert = soil
    found = False

    for map in maps[2]:
        if fert >= map[1] and fert <= map[1] + map[2] - 1:
            water = map[0] + (fert - map[1])
            found = True
    if not found:
        water = fert
    found = False

    for map in maps[3]:
        if water >= map[1] and water <= map[1] + map[2] - 1:
            light = map[0] + (water - map[1])
            found = True
    if not found:
        light = water
    found = False

    for map in maps[4]:
        if light >= map[1] and light <= map[1] + map[2] - 1:
            temp = map[0] + (light - map[1])
            found = True
    if not found:
        temp = light
    found = False

    for map in maps[5]:
        if temp >= map[1] and temp <= map[1] + map[2] - 1:
            humid = map[0] + (temp - map[1])
            found = True
    if not found:
        humid = temp
    found = False

    for map in maps[6]:
        if humid >= map[1] and humid <= map[1] + map[2] - 1:
            loc = map[0] + (humid - map[1])
            found = True
    if not found:
        loc = humid
    found = False

    locations.append(loc)

print(locations)
print("min", min(locations))
types = ["soil", "fert", "water", "light", "temp", "humid", "loc"]

nStarts = [[starts[i], starts[i] + starts[i+1]] for i in range(0, len(starts), 2)]

locationRanges = []
def mapTo(list):
    start = list[0]
    end = list[1]

    for mapIndex in range(0, 7):
        for map in maps[mapIndex]:
            if start >= map[1] and start <= map[1] + map[2] - 1:
                if end <= map[1] + map[2] - 1:
                    diff = map[1] - map[0]
                    start -= diff
                    end -= diff
                else:
                    diff = map[1] - map[0]
                    mapTo([map[1] + map[2], end])
                    start -= diff
                    end = map[1] + map[2] - 1 - diff
                break
            elif end >= map[1] and end <= map[1] + map[2] - 1:
                # start of input doesn't start in the middle of a map but the end does
                diff = map[1] - map[0]
                mapTo([start, map[1]-1])
                start = map[1]-diff
                end -= diff

                break
            elif start >= map[1] and end <=  map[1] + map[2] - 1:
                # a range is fully encapsulated within the input
                diff = map[1] - map[0]
                mapTo([start, map[1]-1])
                mapTo([map[1] + map[2], end])
                start = map[1] - diff
                end = map[1] + map[2] - 1 - diff

                break

    locationRanges.append([start, end])

for start in nStarts:
    mapTo(start)
        
print(locationRanges)
# 529571705 too high