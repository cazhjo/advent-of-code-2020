import input
data = input.get_data("15")

def number_game(starting_numbers, end):
    game_arr = starting_numbers
    last_number = 14
    index = len(game_arr)
    game_arr[0] = [4, 4] 
    while index < end:
        index += 1
        if len(game_arr[last_number]) > 1:
            next_number = (index - (game_arr[last_number][0] + 1))
            if next_number in game_arr:
                if len(game_arr[next_number]) > 1:
                    game_arr[next_number] = [game_arr[next_number][1], index]
                else:     
                    game_arr[next_number] = [game_arr[next_number][0], index]
            else:
                game_arr[next_number] = [index]
            last_number = next_number
        else:
            game_arr[0] = [game_arr[0][1], index]
            last_number = 0

    return last_number

def convert_to_dict(numbers):
    dictionary = {}
    for i, number in enumerate(numbers):
        dictionary[number] = [i + 1]
    
    return dictionary

data = convert_to_dict(list(map(lambda x: int(x), data[0].split(","))))
print("Part1:", number_game(data, 2020))
print("Part2:", number_game(data, 30000000))