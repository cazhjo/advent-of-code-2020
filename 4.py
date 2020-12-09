import input as ind
import re

data = ind.get_data("4")

def extraValidation(key, value):
    valid = True
    
    if key == "byr":
        valid = len(value) == 4 and int(value) >= 1920 and int(value) <= 2002
    elif key == "iyr":
        valid = len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
    elif key == "eyr":
        valid = len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
    elif key == "hgt":
        unit = value[-2:]
        if unit == "cm":
            valid = int(value[:-2]) >= 150 and int(value[:-2]) <= 193
        elif unit == "in":
            valid = int(value[:-2]) >= 59 and int(value[:-2]) <= 76
        else:
            valid = False
    elif key == "hcl":
        if value[0] == "#":
            regexp = re.compile(r'([g-z])')
            
            if int(value[1:], 16) and len(value[1:]) == 6:
                valid = True
            else:
                print("here")
                valid = False
        else:
            valid = False
    elif key == "ecl":
        regexp = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
        if regexp.search(value):
            valid = True
        else:
            valid = False
    elif key == "pid":
        try:
            valid = len(value) == 9
        except ValueError:
            valid = False

        
    return valid

        

def isValid(passport, extra):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    valid = True
    for field in requiredFields:
        if field in passport:
            if extra:
                if not extraValidation(field, passport[field]):
                    valid = False
                    break
            continue
        else:
            if field != "cid":
                valid = False

    return valid

def collect_passports(data):
    passports = []
    passport = {} 
    
    for item in data:
        if item == "":
            passports.append(passport)
            passport = {}
            continue
        for item2 in item.split(" "):
            arr = item2.split(":")
            passport[arr[0]] = arr[1]

    passports.append(passport) #skipped last
    return passports

def countValidPassports(inp, extra):
    valid_count = 0
    for passport in inp:
        if isValid(passport, extra):
            valid_count += 1

    return valid_count

data = collect_passports(data)
part1 = countValidPassports(data, False)
part2 = countValidPassports(data, True)

print("part1: %s" % part1)
print("part2: %s" % part2)

