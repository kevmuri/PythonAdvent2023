inputFile = open("day1-1-input.txt", "r")
lines = inputFile.readlines()

count = 0
for line in lines:
    digits = []
    for i in line:
        if i.isnumeric():
            digits.append(i)
    firstDigit = digits[0]
    lastDigit = digits[-1]
    numberToAdd = int(str(firstDigit) + str(lastDigit))
    count += numberToAdd

print(count)
