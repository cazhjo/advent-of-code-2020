import input
data = input.get_data("1")

part1 = 0
part2 = 0

data = list(map(int, data))

for x in data:
    for y in data:
        if x + y == 2020:
            part1 = x * y
        for z in data:
            if x + y + z == 2020:
                part2 = x * y * z

print("part1: %d" % part1)
print("part2: %d" % part2)