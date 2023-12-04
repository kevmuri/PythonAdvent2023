import re


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
    for line in range(len(lines)):
        lines[line] = "." + lines[line] + "."

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
        found_numbers_in_row = [item for item in set(found_numbers_in_row)]
        found_numbers_in_input.append(found_numbers_in_row)

    return found_numbers_in_input


def main():
    answer = 0
    lines = read_file()
    found_numbers_in_input = get_numbers_to_check_for(lines)
    for idx, number_row in enumerate(found_numbers_in_input):
        for number in number_row:
            parsers = [
                m.start()
                for m in re.finditer(
                    rf"\D{number}\D",
                    lines[idx],
                )
            ]
            for parser in parsers:
                parser = parser + 1
                for digit in number:
                    border_chars = [
                        lines[idx - 1][parser - 1],  # top left
                        lines[idx - 1][parser],  # top
                        lines[idx - 1][parser + 1],  # top right
                        lines[idx][parser - 1],  # left
                        lines[idx][parser + 1],  # right
                        lines[idx + 1][parser - 1],  # bottom left
                        lines[idx + 1][parser],  # bottom
                        lines[idx + 1][parser + 1],  # bottom right
                    ]
                    symbol_found = False
                    for char in border_chars:
                        if not char.isnumeric() and char != "." and char != "\n":
                            answer += int(number)
                            symbol_found = True
                            break
                    parser = parser + 1
                    if symbol_found:
                        break
    print(answer)


main()
