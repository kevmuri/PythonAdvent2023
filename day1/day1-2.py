inputFile = open("day1-input.txt", "r")
lines = inputFile.readlines()

digitDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

count = 0
for line in lines:
    for digitDictItem in digitDict.keys():
        if digitDictItem in line:
            # These strings rely on the letters before and after, so would eight8eightwo2two be valid?
            newString = digitDictItem + str(digitDict[digitDictItem]) + digitDictItem
            line = line.replace(digitDictItem, newString)

    digits = []
    for char in line:
        if char.isnumeric():
            digits.append(char)
    firstDigit = digits[0]
    lastDigit = digits[-1]
    numberToAdd = int(str(firstDigit) + str(lastDigit))
    print(numberToAdd)
    count += numberToAdd

print(count)
