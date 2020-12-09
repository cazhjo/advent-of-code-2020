import input
import math

data = input.get_data("5")

def find_number_in_string(ranges, lower, upper, string):
    start = ranges
    for char in string:
        if char == lower:
            start[1] = math.floor((start[0] + start[1]) / 2)
        elif char == upper:
            start[0] = math.ceil((start[0] + start[1]) / 2)

    return start[0] if start[0] != 0 else start[1]


def find_highest_seat(inp):
    maximum = 0
    for line in inp:
        current = find_number_in_string([0, 127], "F", "B", line[:-3]) * 8 + find_number_in_string([0, 7], "L", "U", line[-3:])
        if current > maximum:
            maximum = current

    return maximum

def find_all_seats(inp, filt):
    seats = []
    for line in inp:
        row = find_number_in_string([0, 127], "F", "B", line[:-3])
        column = find_number_in_string([0, 7], "L", "U", line[-3:])
        seat_id = row * 8 + column
        
        if filt == "both":
            seats.append([row, column])
        elif filt == "column":
            seats.append(column)
        elif filt == "row":
            seats.append(row)
        elif filt == "id":
            seats.append(seat_id)

    return seats

def find_missing_seat(seats):
    possible = []
    count = 0
    current = 2
    for seat in seats:
        if seat[0] == 1 or seat[0] == 110 or seat[0] < 2:
            continue
        
        if seat[0] != current:
            if count < 8:
                break
            else:
                count = 0
                current = seat[0]
                possible = []

        current = seat[0]
        count += 1
        possible.append(seat)

    return possible
        
        


seats = find_all_seats(data, "both")
seats.sort(key=lambda x: x[0])
part1 = find_highest_seat(data)
part2 = find_missing_seat(seats)

print("part1:", part1)
print("part2:", part2[2][0] * 8 + part2[2][1])