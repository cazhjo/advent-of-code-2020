import input
import math

def rotate_a(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

data = input.get_data("12")
def get_direction(facing):
    direction = ""
    if facing == 0:
        direction = "E"
    elif facing == 90:
        direction = "S"
    elif facing == 180 or facing == -180:
        direction = "W"
    else:
        direction = "N"
    return direction

def convert_format(facing):
    while(facing > 180):
        facing -= 360
    return facing

def rotate(letter, value, facing):
    if letter == 'R':
        facing += value
        if facing > 180:
            facing -= 360
    if letter == 'L':
        facing -= value
        if facing < 180:
            facing += 360

    return facing

def count_instructions(ins):
    directions = {"E": 0, "N": 0, "W": 0, "S": 0}
    direction = "E"
    facing = 0

    for instruction in ins:
        letter = list(instruction)[0]
        value = int(instruction[1:])
        facing = rotate(letter, value, facing)
        facing = convert_format(facing)
        direction = get_direction(facing)
        
        if letter == 'F':
            directions[direction] += value
        elif letter in directions:
            directions[letter] += value

    manhattan = abs(directions["E"] - directions["W"]) + abs(directions["N"] - directions["S"])
    return manhattan

def get_opposite(letter):
    opposite = ""
    if letter == "E":
        opposite = "W"
    if letter == "S":
        opposite = "N"
    if letter == "W":
        opposite = "E"
    if letter == "N":
        opposite = "S"
    return opposite

def move_relative(ins):
    directions = {"E": 0, "N": 0, "W": 0, "S": 0}
    waypoint = {"E": 10, "N": 1, "W": 0, "S": 0}
    facing = 0

    for instruction in ins:
        letter = list(instruction)[0]
        value = int(instruction[1:])
        facing = rotate(letter, value, facing)
        facing = convert_format(facing)
        if letter == "R" or letter == "L":
            if letter == "L":
                new = rotate_a((0, 0), (waypoint["E"], waypoint["N"]), math.radians(value))    
            elif letter == "R":
                new = rotate_a((0, 0), (waypoint["E"], waypoint["N"]), math.radians(-value))    
            waypoint["E"] = round(new[0])
            waypoint["N"] = round(new[1])

        if letter == 'F':
            directions["E"] += value * waypoint["E"]
            directions["N"] += value * waypoint["N"]
        elif letter in waypoint:
            if letter == "S":
                waypoint["N"] -= value
            elif letter == "W":
                waypoint["E"] -= value
            else:
                waypoint[letter] += value 

    manhattan = abs(directions["E"]) + abs(directions["N"])
    return manhattan
    

print("Part1:", count_instructions(data))
print("Part2:", move_relative(data))
        
        
            