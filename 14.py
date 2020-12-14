import input
from functools import reduce
import itertools
data = input.get_data("14")

def apply_bitmask_to_value(numbers):
    currentMask = ""
    mem = {}
    for line in numbers:
        arr = line.split("=")
        key = arr[0].strip()
        value = arr[1].strip()
        if key == "mask":
            currentMask = value
            continue
        key = key[4:-1]
        binary = bin(int(value))[2:]
        binary = list((36 - len(binary)) * "0" + binary)
        for i, char in enumerate(binary):
            if currentMask[i] == "X":
                continue
            binary[i] = currentMask[i]
        mem[key] = int("".join(binary), 2)

    return reduce(lambda x, value: x + value, mem.values(), 0)

def apply_bitmask_to_address(numbers):
    currentMask = ""
    mem = {}
    for line in numbers:
        arr = line.split("=")
        key = arr[0].strip()
        value = arr[1].strip()
        if key == "mask":
            currentMask = value
            continue
        key = key[4:-1]
        binary = bin(int(key))[2:]
        binary = list((36 - len(binary)) * "0" + binary)
        countX = 0
        for i, char in enumerate(binary):
            if currentMask[i] == "X":
                binary[i] = "X"
                countX +=1
                continue
            binary[i] = currentMask[i] if currentMask[i] == "1" else binary[i]

        for x in itertools.product([0, 1], repeat=countX):
            temp = binary[:]
            count = countX
            for i, char in enumerate(temp):
                if char == "X":
                    temp[i] = str(x[(countX - 1) - (count - 1)])
                    count -= 1
            address = str(int("".join(temp), 2))
            mem[address] = int(value)

    return reduce(lambda x, value: x + value, mem.values(), 0)

print("Part1:", apply_bitmask_to_value(data))
print("Part2:", apply_bitmask_to_address(data))
            