import input
from functools import reduce

data = input.read_data(str)

def findRules(bag):
    for rule in data:
        name = rule.split("contain")[0].rstrip()
        if name[len(name) - 1] == "s":
            name = name[:len(name) - 1]

        if name in bag:
            return rule

def contains_bag(startingBag, bagType):
    if startingBag == " other bags":
        return False
    
    rule = findRules(startingBag)
    print(startingBag)
    if bagType in rule[1]:
        return True
    else:
        return False

def handle_bags(bags, bagType):
    current = False
    
    for bag in bags:
        if bag == " no other bags.":
            current = False
            break

        if bagType in bag:
            current = True
            break
        fixedBag = bag[3:].replace(".", "")
        rule = findRules(fixedBag)
        newBags = rule.split("contain")[1].split(",")
        if bagType in str(newBags):
            current = True
            break
        else:
            temp = handle_bags(newBags, bagType)
            if temp:
                current = True
                break
            else:
                current = False
                continue

    return current

def count_shiny(rules, bagType):
    count = 0
    for i, item in enumerate(rules):
        if item == "":
            continue
        bags = item.split("contain")[1].split(",")

        contains = handle_bags(bags, bagType)
        if contains:
            count += 1
        
        print(i)

    print(count)

holder = {}
def count_all(entry):
    rule = findRules(entry)
    ruleName = rule.split("contain")[0].rstrip()
    bags = rule.split("contain")[1].split(",")
    count = 0
    rowNumbers = []
    # if len(bags) > 1:
    #     parentRuleName = ruleName
    # else:
    #     ruleName = parentRuleName
    for i, bag in enumerate(bags):
        # if i > 0 and parent != 0:
        #     holder[ruleName].append(int(parent))

        if bag == " no other bags.":
            count = 0
            break
        
        number = int(bag.split(" ")[1])
        rowNumbers.append(number)
        #holder[ruleName].append(int(number))
        name = " ".join(bag.split(" ")[2:]).replace(".", "")
        # if ruleName not in holder:
        #     holder[ruleName] = [int(number)]
        # else:
        #     holder[ruleName].append(int(number))
        temp = count_all(name)
        count += number + number * temp if temp != 0 else number * 1 

        # if i > 0 and holder[ruleName][-1] == 0:
        #     holder[ruleName][holder[ruleName].index(0) - 1] += holder[ruleName][-2]
        #     del holder[ruleName][-2]
    # print(rowNumbers)
    # temp = reduce(lambda x, y: x + y, rowNumbers) if len(rowNumbers) > 0 else 0
    return count
        



print(count_all("shiny gold bags"))
# holder = ",".join(map(lambda x: str(x), holder)).split("0")
# count = 0

# for key, value in holder.items():
#     if 0 in value and len(value) > 1:
#         count += reduce(lambda x, y: y + x * y, list(filter(lambda x: x != 0, value)))
#     # else:
#     #     count += reduce(lambda x, y: x + y, value)

# print(count)

# for item in holder:
#     newItem = item[::-1]
#     if newItem == "":
#         break
#     temp = int(newItem[1])
#     for char in range(2, len(newItem)):
#         if(newItem[char] == ","):
#             continue
#         temp = int(newItem[char]) + temp * int(newItem[char])

#     count += temp

# print(count)
        