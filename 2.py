import input

data = input.get_data("2")

def correctCount(range, letter, password):
    count = password.count(letter)
    return count >= range[0] and count <= range[1]


def passwordHasOnlyOne(indices, letter, password):
    return (int(password[indices[0] - 1] == letter) + int(password[indices[1] - 1] == letter)) == 1


def getValues(line):
    colon = line.index(':')
    dash = line.split('-')
    first = int(dash[0])
    second = int(dash[1].split(' ')[0])
    letter = line[colon - 1]
    password = line[colon + 2:]

    return {"first": first, "second": second, "letter": letter, "password": password}


def part1(data):
    valid = 0
    for item in data:
        values = getValues(item)
        valid = (valid + 1 if correctCount([values["first"], values["second"]], values["letter"], values["password"]) else valid)
    
    return valid


def part2(data):
    valid = 0
    for item in data:
        values = getValues(item)
        valid = (valid + 1 if passwordHasOnlyOne([values["first"], values["second"]], values["letter"], values["password"]) else valid)

    return valid


print("part1: %s" % part1(data))
print("part2: %s" % part2(data))

