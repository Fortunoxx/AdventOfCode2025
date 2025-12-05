def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        positions = {}
        y = 0
        for line in file:
            x = 0
            for char in line.strip():
                if char == "@":
                    positions[(x, y)] = "@"
                x += 1
            y += 1
        return positions


def calc(positions, max=4):
    allowed = []
    for pos in positions:
        cnt = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                newPos = (x + pos[0], y + pos[1])
                if newPos in positions and newPos != pos:
                    cnt += 1
        if cnt < max:
            allowed.append(pos)
    return allowed

def calc2(positions):
    removed = 0
    removing = calc(positions)
    removed += len(removing)

    while len(removing) > 0:
        for pos in removing:
            del positions[pos]
        removing = calc(positions)
        removed += len(removing)
    return removed


def solve_part1(fileInfo):
    positions = get_values(fileInfo)
    allowed = calc(positions)
    return len(allowed)


def solve_part2(fileInfo):
    positions = get_values(fileInfo)
    return calc2(positions)
