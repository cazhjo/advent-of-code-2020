import input

data = input.read_data()

def count(questions):
    used = []
    count = 0

    for question in questions:
        if question == "\n":
            used = []
            continue

        for letter in question:
            if letter in used or letter == "\n":
                continue

            count += 1
            used.append(letter)

    return count

def getGroups(questions):
    groups = []
    temp = []
    
    for question in questions:
        if question == "\n":
            groups.append(temp)
            temp = []
            continue

        temp.append(question)

    groups.append(temp)

    return groups

def countAll(groups):
    
    count = 0
    for group in groups:
        if len(group) == 1:
            count += len(set(group[0])) - 1
            continue
        print("")
        for letter in set(group[0]):
            if letter == "\n":
                continue
            everyone = True
            for j in range(1, len(group)):
                print(group[j])
                if letter not in group[j]:
                    everyone = False
                    break
            
            count += 1 if everyone else 0

    print(count)

countAll(getGroups(data))



