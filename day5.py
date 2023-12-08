from multiprocessing import Pool
import time

# print(maps)
# # print(starts)
# for seed in starts:
#     for map in maps[0]:
#         if seed >= map[1] and seed <= map[1] + map[2] - 1:
#             soil = map[0] + (seed - map[1])
#             found = True
#     if not found:
#         soil = seed
#     # print(soil)
#     found = False

#     for map in maps[1]:
#         if soil >= map[1] and soil <= map[1] + map[2] - 1:
#             fert = map[0] + (soil - map[1])
#             found = True
#     if not found:
#         fert = soil
#     found = False

#     for map in maps[2]:
#         if fert >= map[1] and fert <= map[1] + map[2] - 1:
#             water = map[0] + (fert - map[1])
#             found = True
#     if not found:
#         water = fert
#     found = False

#     for map in maps[3]:
#         if water >= map[1] and water <= map[1] + map[2] - 1:
#             light = map[0] + (water - map[1])
#             found = True
#     if not found:
#         light = water
#     found = False

#     for map in maps[4]:
#         if light >= map[1] and light <= map[1] + map[2] - 1:
#             temp = map[0] + (light - map[1])
#             found = True
#     if not found:
#         temp = light
#     found = False

#     for map in maps[5]:
#         if temp >= map[1] and temp <= map[1] + map[2] - 1:
#             humid = map[0] + (temp - map[1])
#             found = True
#     if not found:
#         humid = temp
#     found = False

#     for map in maps[6]:
#         if humid >= map[1] and humid <= map[1] + map[2] - 1:
#             loc = map[0] + (humid - map[1])
#             found = True
#     if not found:
#         loc = humid
#     found = False

#     locations.append(loc)

# # print(locations)
# print("min", min(locations))
# # types = ["soil", "fert", "water", "light", "temp", "humid", "loc"]

# nStarts = [[starts[i], starts[i] + starts[i+1] - 1] for i in range(0, len(starts), 2)]
# # print(nStarts)
# locationRanges = []
# def mapTo(list, mapIndex):
#     start = list[0]
#     end = list[1]
#     targetMap = maps[mapIndex]
#     results = []
#     startFound = False
#     endFound = False
#     for map in targetMap:
#         if start >= map[1] and start <= map[1] + map[2] - 1:
#             startFound = True
#             if end >= map[1] and end <= map[1] + map[2] - 1:
#                 results.append([start + (map[0] - map[1]), end + (map[0] - map[1])])
#             else:
#                 results.append([start + (map[0] - map[1]), map[0] + map[2] - 1])
#                 for result in mapTo([map[0] + map[2], end], mapIndex):
#                     results.append(result)

#     if not startFound:
#         for map in targetMap:
#             if end >= map[1] and end <= map[1] + map[2] - 1:
#                 endFound = True
#                 results.append([map[0] + map[2], end + (map[0] - map[1])])
#                 for result in mapTo([start, map[1] + map[2] - 1], mapIndex):
#                     results.append(result)
    
#     if not startFound and not endFound:
#         results.append([start, end])
                
#     return results

# locationRanges = []
# one = mapTo([49, 97], 0)
# print(one)

# # 529571705 too high

# EVERYTHING SUCKS ITS BRUTE FORCE TIME

# for i in range(0, len(starts), 2):
#     for seed in range(starts[i], starts[i] + starts[i+1] - 1):
#         for map in maps[0]:
#             if seed >= map[1] and seed <= map[1] + map[2] - 1:
#                 soil = map[0] + (seed - map[1])
#                 found = True
#         if not found:
#             soil = seed
#         # print(soil)
#         found = False

#         for map in maps[1]:
#             if soil >= map[1] and soil <= map[1] + map[2] - 1:
#                 fert = map[0] + (soil - map[1])
#                 found = True
#         if not found:
#             fert = soil
#         found = False

#         for map in maps[2]:
#             if fert >= map[1] and fert <= map[1] + map[2] - 1:
#                 water = map[0] + (fert - map[1])
#                 found = True
#         if not found:
#             water = fert
#         found = False

#         for map in maps[3]:
#             if water >= map[1] and water <= map[1] + map[2] - 1:
#                 light = map[0] + (water - map[1])
#                 found = True
#         if not found:
#             light = water
#         found = False

#         for map in maps[4]:
#             if light >= map[1] and light <= map[1] + map[2] - 1:
#                 temp = map[0] + (light - map[1])
#                 found = True
#         if not found:
#             temp = light
#         found = False

#         for map in maps[5]:
#             if temp >= map[1] and temp <= map[1] + map[2] - 1:
#                 humid = map[0] + (temp - map[1])
#                 found = True
#         if not found:
#             humid = temp
#         found = False

#         for map in maps[6]:
#             if humid >= map[1] and humid <= map[1] + map[2] - 1:
#                 loc = map[0] + (humid - map[1])
#                 found = True
#         if not found:
#             loc = humid
#         found = False

#         locations.append(loc)
locs = []
mpStarts = [280775197, 7535297, 3229061264, 27275209, 77896732, 178275214, 2748861189, 424413807, 3663093536, 130341162, 613340959, 352550713, 1532286286, 1115055792, 1075412586, 241030710, 3430371306, 138606714, 412141395, 146351614]
# mpStarts = [79, 14, 55, 13]

def calculateSeed(index):

    file = open("day5.txt")
    inputFile = []
    linesInFile = file.readlines()
    for i in linesInFile:
        inputFile.append(format(i.strip()))

    # starts = [79, 14, 55, 13]
    starts = [280775197, 7535297, 3229061264, 27275209, 77896732, 178275214, 2748861189, 424413807, 3663093536, 130341162, 613340959, 352550713, 1532286286, 1115055792, 1075412586, 241030710, 3430371306, 138606714, 412141395, 146351614]
    locations = []
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


    for seed in range(starts[index], starts[index] + starts[index+1] - 1):
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

    return min(locations)

finalLocs = []

if __name__ == "__main__":
    deltaTimeStart = time.time()
    with Pool(10) as p:
        finalLocs = p.map(calculateSeed, [i for i in range(0, len(mpStarts), 2)])

# print(finalLocs)
if len(finalLocs) != 0:
    minimum = finalLocs[0]
    for i in finalLocs:
        if i < minimum:
            minimum = i
    print("a", minimum)
# 6089325 too high
# 6082925 too high