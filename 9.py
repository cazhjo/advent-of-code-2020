import input

data = input.get_data("9")

def doesNumberSum(numbers, number):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers)):
            if i == j:
                continue
            if int(numbers[i]) + int(numbers[j]) == int(number):
                return True
    else:
        return False

def findContiguousSum(numbers, invalidNumber):
    conRange = []
    tempSum = []
    
    for i in range(len(numbers) - 1):
        conRange = [int(numbers[i])]
        tempSum = int(numbers[i])
        for j in range(i + 1, len(numbers)):
            if i == j:
                continue
            conRange.append(int(numbers[j]))
            tempSum += int(numbers[j])
            if tempSum == int(invalidNumber):
                return min(conRange) + max(conRange)
            

def first_fail(numbers, preamble):

    for i in range(preamble, len(numbers)):
        if not doesNumberSum(numbers[i - preamble: i], numbers[i]):
            return numbers[i]

part1 = first_fail(data, 25)
part2 = findContiguousSum(data, part1)

print("part1: %s" % part1)
print("part2: %s" % part2)