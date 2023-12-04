import re


def read_file():
    input_file = open("day3-input-example.txt", "r")
    lines = input_file.readlines()

    # Add border of periods beginning with rows
    border_row = ""
    for i in range(len(lines[0])):
        border_row += "."
    lines.append(border_row)
    lines.insert(0, border_row)
    # Add columns on sides
    for line in range(len(lines)):
        lines[line] = lines[line].replace("*", "G")
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


def added_numbers():
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
                        if (
                            not char.isnumeric()
                            and char != "."
                            and char != "\n"
                            and char != "G"
                        ):
                            answer += int(number)
                            symbol_found = True
                            break
                    parser = parser + 1
                    if symbol_found:
                        break
    return answer


def string_to_array(number_string):
    number_string_to_array = number_string.split(".")
    new_array = []
    for i in number_string_to_array:
        if i != "":
            new_array.append(i)

    return new_array


def main():
    answer = added_numbers()
    lines = read_file()
    for line_idx, line in enumerate(lines):
        parsers = [m.start() for m in re.finditer(r"G", line)]
        for parser in parsers:
            found_numbers = []
            # Get top numbers, starting with middle
            number_string = lines[line_idx - 1][parser]
            # Get top characters; left
            parser_position = parser - 1
            current_char = lines[line_idx - 1][parser_position]
            while current_char.isnumeric():
                number_string = current_char + number_string
                parser_position = parser_position - 1
                current_char = lines[line_idx - 1][parser_position]
            # Get top characters, right
            parser_position = parser + 1
            current_char = lines[line_idx - 1][parser_position]
            while current_char.isnumeric():
                number_string = number_string + current_char
                parser_position = parser_position + 1
                current_char = lines[line_idx - 1][parser_position]
            if string_to_array(number_string):
                for number in string_to_array(number_string):
                    found_numbers.append(number)

            # Get bottom numbers, starting with middle
            number_string = lines[line_idx + 1][parser]
            # Get top characters; left
            parser_position = parser - 1
            current_char = lines[line_idx + 1][parser_position]
            while current_char.isnumeric():
                number_string = current_char + number_string
                parser_position = parser_position - 1
                current_char = lines[line_idx + 1][parser_position]
            # Get top characters, right
            parser_position = parser + 1
            current_char = lines[line_idx + 1][parser_position]
            while current_char.isnumeric():
                number_string = number_string + current_char
                parser_position = parser_position + 1
                current_char = lines[line_idx + 1][parser_position]
            if string_to_array(number_string):
                for number in string_to_array(number_string):
                    found_numbers.append(number)

            # Get left number
            number_string = ""
            parser_position = parser - 1
            current_char = lines[line_idx][parser_position]
            while current_char.isnumeric():
                number_string = current_char + number_string
                parser_position = parser_position - 1
                current_char = lines[line_idx][parser_position]
            if string_to_array(number_string):
                for number in string_to_array(number_string):
                    found_numbers.append(number)

            # Get right number
            number_string = ""
            parser_position = parser + 1
            current_char = lines[line_idx][parser_position]
            while current_char.isnumeric():
                number_string = number_string + current_char
                parser_position = parser_position + 1
                current_char = lines[line_idx][parser_position]
            if string_to_array(number_string):
                for number in string_to_array(number_string):
                    found_numbers.append(number)

            # Adjust answer
            print(found_numbers)
            if len(found_numbers) == 2:
                product = int(found_numbers[0]) * int(found_numbers[1])
                print("product", product)
                answer = answer + product
            elif found_numbers:
                answer = int(found_numbers[0]) + answer
    print(answer)


main()
