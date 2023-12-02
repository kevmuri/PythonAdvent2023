# 12 red
# 13 green
# 14 blue
def process_input():
    input_file = open("day2-input.txt", "r")
    lines = input_file.readlines()

    input_array = []

    for line in lines:
        line = line.split(":")
        hands = line[1].split(";")
        # Each game is an array of hands
        hand_array = []
        for hand in hands:
            cube_counts = hand.split(",")
            # A hand is a dictionary with colors and their counts
            cube_count_object = {"red": 0, "green": 0, "blue": 0}
            for cube_count in cube_counts:
                cube_count = cube_count.replace("\n", "")
                cube_count = cube_count.replace(" ", "", 1)
                cube_count_split = cube_count.split(" ")
                cube_count_object[cube_count_split[1]] = cube_count_split[0]
            hand_array.append(cube_count_object)
        input_array.append(hand_array)

    return input_array


def main():
    maximums = {"red": 12, "green": 13, "blue": 14}

    games = process_input()
    added_id = 0
    for game in games:
        possible = True
        for hand in game:
            for color in hand.keys():
                if int(hand[color]) > maximums[color]:
                    possible = False
        if possible:
            added_id += games.index(game) + 1
    print(added_id)


main()
