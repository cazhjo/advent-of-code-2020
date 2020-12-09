import input
data = input.get_data("3")

def slopeDown(rule, input):
    index = [0, 0]
    size = 1
    trees = 0
    while(True):
        index[0] += rule[0]
        index[1] += rule[1]
        if index[1] > len(input) - 1:
            break

        if index[0] > len(input[index[1]]) - 1:
            size += 1

        input[index[1]] = input[index[1]] * size

        if input[index[1]][index[0]] == "#":
            trees += 1

    return trees

part1 = slopeDown([3, 1], data)
part2 = slopeDown([1, 1], data) * part1 * slopeDown([5, 1], data) * slopeDown([7, 1], data) * slopeDown([1, 2], data)

print("part1: %s" % part1)
print("part2: %s" % part2)