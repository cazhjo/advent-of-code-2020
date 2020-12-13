import input

data = input.get_data("13")

def add_id_until_number(Id, number):
    originalId = Id
    while Id <= number:
        Id += originalId

    return Id


def find_earliest_possible(inp):
    minimum = 100000000000000000000
    minId = 0
    for Id in inp[1].split(","):
        if Id == "x":
            continue
        newNum = add_id_until_number(int(Id), int(inp[0]))
        if newNum <= minimum:
            minimum = newNum
            minId = Id
    return int(minId) * (int(minimum) - int(inp[0]))


def find_earliest_order(inp):
    originalNum = int(inp[0])
    rootNum = 0
    isCorrect = True
    arr = inp.split(",")
    while True:
        for index in range(1, len(arr)):
            if arr[index] == "x":
                continue
            if (rootNum + index) % int(arr[index]) != 0:
                isCorrect = False
                break
        if isCorrect:
            break
        rootNum += originalNum
        isCorrect = True

    return rootNum

print(find_earliest_possible(data)) # Part 1
# print(find_earliest_order(data[1])) # Part 2