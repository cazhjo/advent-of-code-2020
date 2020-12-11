import input
import time
data = input.get_data("11")

def isOccupied(seat):
    if seat == None:
        return 0
    return 1 if seat == "#" else 0

def change_adjacent(rows):
    new = []
    changed = False
    for x, row in enumerate(rows):
        string = ""
        for y, column in enumerate(row):
            if column == ".":
                string += "."
                continue
            left = row[y - 1] if y > 0 else None
            right = row[y + 1] if y < len(row) - 1 else None
            down = rows[x + 1][y] if x < (len(rows) - 1) else None
            up = rows[x - 1][y] if x > 0 else None
            diagUl = rows[x - 1][y - 1] if x > 0 and left != None else None
            diagUr = rows[x - 1][y + 1] if x > 0 and right != None else None
            diagDl = rows[x + 1][y - 1] if x < len(rows) - 1 and left != None else None
            diagDr = rows[x + 1][y + 1] if x < len(rows) - 1 and right != None else None
            occupiedAdjacents = 0
            isEmpty = column == "L"

            occupiedAdjacents += isOccupied(left)
            occupiedAdjacents += isOccupied(right)
            occupiedAdjacents += isOccupied(down)
            occupiedAdjacents += isOccupied(up)
            occupiedAdjacents += isOccupied(diagUl)
            occupiedAdjacents += isOccupied(diagUr)
            occupiedAdjacents += isOccupied(diagDl)
            occupiedAdjacents += isOccupied(diagDr)

            if isEmpty and occupiedAdjacents == 0:
                string += "#"
                changed = True
            elif not isEmpty and occupiedAdjacents >= 4:
                string += "L"
                changed = True
            else:
                string += column
                continue
        new.append(string)

    return [new, changed]

def count_visible_direction(original, seatIndices, x_inc, y_inc):
    currentSeat = seatIndices[:]
    while True:
        currentSeat[0] += x_inc
        currentSeat[1] += y_inc
        if currentSeat[0] < 0 or currentSeat[0] > len(original) - 1:
            return 0
        elif currentSeat[1] < 0 or currentSeat[1] > len(original[currentSeat[0]]) - 1:
            return 0

        newSeat = original[currentSeat[0]][currentSeat[1]]
        if newSeat == "L":
            return 0
        elif newSeat == "#":
            return 1 

def change_adjacent_direction(rows):
    new = []
    changed = False
    for x, row in enumerate(rows):
        string = ""
        for y, column in enumerate(row):
            if column == ".":
                string += "."
                continue
            occupiedAdjacents = 0
            isEmpty = column == "L"

            occupiedAdjacents += count_visible_direction(rows, [x, y], 0, -1)
            occupiedAdjacents += count_visible_direction(rows, [x, y], -1, 0)
            occupiedAdjacents += count_visible_direction(rows, [x, y], 0, 1)
            occupiedAdjacents += count_visible_direction(rows, [x, y], 1, 0)
            occupiedAdjacents += count_visible_direction(rows, [x, y], -1, -1)
            occupiedAdjacents += count_visible_direction(rows, [x, y], -1, 1)
            occupiedAdjacents += count_visible_direction(rows, [x, y], 1, 1)
            occupiedAdjacents += count_visible_direction(rows, [x, y], 1, -1)
            if isEmpty and occupiedAdjacents == 0:
                string += "#"
                changed = True
            elif not isEmpty and occupiedAdjacents >= 5:
                string += "L"
                changed = True
            else:
                string += column
                continue
        new.append(string)

    return [new, changed]

def change_until_no_change(original, isPart1):
    new = original[:]
    while True:
        temp = change_adjacent(new) if isPart1 else change_adjacent_direction(new)
        new = temp[0][:]
        if not temp[1]:
            break

    return new

def count_occupied(rows):
    count = 0
    for row in rows:
        for column in row:
            if column == "#":
                count +=1
    
    return count

part1 = count_occupied(change_until_no_change(data, True))
part2 = count_occupied(change_until_no_change(data, False))
print(part1)
print(part2)