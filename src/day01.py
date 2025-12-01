def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        return [(-1 if line[0] == "L" else 1) * int(line.strip()[1:]) for line in file]

def calc(instructions, position = 0):
    zeroes = 0;
    for i in instructions:
        position += i
        while position >= 100:
            position -= 100
        while position < 0:
            position += 100
        if position == 0:
            zeroes += 1
    return zeroes


def calc2(instructions, position = 0):
    zeroes = 0;
    for i in instructions:
        position += i
        while position >= 100:
            position -= 100
            zeroes += 1
        while position < 0:
            position += 100
            zeroes += 1
    return zeroes


def solve_part1(fileInfo):
    instructions = get_values(fileInfo)
    return calc(instructions, 50)


def solve_part2(fileInfo):
    instructions = get_values(fileInfo)
    return calc2(instructions, 50)