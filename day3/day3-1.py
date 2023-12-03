def read_file():
    input_file = open("day3-input.txt", "r")
    lines = input_file.readlines()

    # Add border of periods beginning with rows
    border_row = ""
    for i in range(len(lines[0])):
        border_row += "."
    lines.append(border_row)
    lines.insert(0, border_row)
    # Add columns on sides
    for line in lines:
        line = "." + line + "."

    return lines


def get_numbers_to_check_for(lines):
    found_numbers_in_input = []
    for row in range(len(lines)):
        found_number = ""
        found_numbers_in_row = []
        for character_parser in range(len(lines[row])):
            char = lines[row][character_parser]
            if char.isnumeric():
                found_number = found_number + char
            elif found_number != "":
                found_numbers_in_row.append(found_number)
                found_number = ""
        found_numbers_in_input.append(found_numbers_in_row)

    return found_numbers_in_input


def main():
    answer = 0
    lines = read_file()
    found_numbers_in_input = get_numbers_to_check_for(lines)
    for number_row in range(len(found_numbers_in_input)):
        for number in range(len(found_numbers_in_input[number_row])):
            for digit in found_numbers_in_input[number_row][number]:
                parser = lines[number_row].find(digit)
                found = False
                border_chars = [
                    lines[number_row - 1][parser - 1],  # top left
                    lines[number_row - 1][parser],  # top
                    lines[number_row - 1][parser + 1],  # top right
                    lines[number_row][parser - 1],  # left
                    lines[number_row][parser + 1],  # right
                    lines[number_row + 1][parser - 1],  # bottom left
                    lines[number_row + 1][parser],  # bottom
                    lines[number_row + 1][parser + 1],  # bottom right
                ]
                print([found_numbers_in_input[number_row][number], digit, border_chars])
                for border_char in border_chars:
                    if (
                        not border_char.isnumeric()
                        and border_char != "."
                        and border_char != "\n"
                    ):
                        answer = answer + int(
                            found_numbers_in_input[number_row][number]
                        )
                        found = True
                        break
                if found:
                    break
    print(answer)


main()
