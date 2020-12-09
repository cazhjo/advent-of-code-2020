import input
data = input.read_data(str)

def find_indices():
    indices = []
    
    for i, item in enumerate(data):
        instruction = item.split(" ")[0]
        if instruction == "jmp" or instruction == "nop":
            indices.append([i, instruction])

    return indices


def run_boot_code(inp):
    accumulator = 0
    visited = []
    i = 0
    instructionSet = []
    codes = inp[:]
    indices = find_indices()
    while i < len(codes):
        if i in visited:
            codes = inp[:]
            value = "jmp" if indices[0][1] == "nop" else "nop"
            codes[indices[0][0]] = codes[indices[0][0]].replace(indices[0][1], value)

            accumulator = 0
            visited = []
            i = 0
            indices = indices[1:]
            continue

        instructionSet = codes[i].split(" ")
        visited.append(i)
        if instructionSet[0] == "acc":
            accumulator += int(instructionSet[1])
            i += 1
        elif instructionSet[0] == "nop":
            i += 1
        elif instructionSet[0] == "jmp":
            i += int(instructionSet[1])

    print(accumulator)


run_boot_code(data)


