def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        splitters = []
        pos = ()
        y = 0
        for line in file:
            x = 0
            for char in line.strip():
                if char == "S":
                    pos = (x, y)
                elif char == "^":
                    splitters.append((x, y))
                x += 1
            y += 1
    return pos, splitters, y


def calc_beam_locations(positions, splitters):
    hit = 0
    newPositions = []
    for p in positions:
        if p in splitters:
            hit += 1
            left = (p[0] - 1, p[1])
            right = (p[0] + 1, p[1])
            newPositions.append(left) if left not in newPositions else None
            newPositions.append(right) if right not in newPositions else None
        else:
            newPositions.append(p) if p not in newPositions else None
    return newPositions, hit


def calc(pos, splitters, maxY):
    hitTotal = 0
    currentY = pos[1]
    newPositions = [pos]
    while currentY < maxY - 1:
        positions, hit = calc_beam_locations(newPositions, splitters)
        newPositions = []
        hitTotal += hit
        for p in positions:
            newPositions.append((p[0], p[1] + 1))
        currentY += 1
    return hitTotal


def solve_part1(fileInfo):
    pos, splitters, maxY = get_values(fileInfo)
    return calc(pos, splitters, maxY)


def solve_part2(fileInfo):
    return 0
