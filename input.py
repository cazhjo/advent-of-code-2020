import json
import requests
session = open(".session").readline()

def handle_data(data):
    return data.split("\n")

def clear_file(file):
    file.seek(0)
    file.truncate()

def get_data(day, demo=False):
    file = "data.json" if not demo else "demo.txt"
    f = open(file, "r+")

    if demo:
        return handle_data("".join(f.readlines()))
    data = json.load(f)
    dayInput = {}

    if day not in data:
        url = "https://adventofcode.com/2020/day/%s/input" % day
        r = requests.get(url, cookies={"session": session})
        clear_file(f)
        dayInput = {day: handle_data(r.text)}
        json.dump(dayInput, f)
    else:
        dayInput = data
    f.close()
    return dayInput[day][:-1]


        



