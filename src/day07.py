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


# positions is a dict of position: {(0,0): 3} means 3 beams at that position
def calc_beam_locations2(positions, splitters):
    newPositions = {}
    for p in positions:
        if p in splitters:
            left = (p[0] - 1, p[1])
            right = (p[0] + 1, p[1])

            leftBeam = (
                newPositions[left] + positions[p]
                if left in newPositions
                else positions[p] 
            )
            rightBeam = (
                newPositions[right] + positions[p]
                if right in newPositions
                else positions[p]
            )

            newPositions[left] = leftBeam
            newPositions[right] = rightBeam
        else:
            newPositions[p] = newPositions[right] + positions[p] if p in newPositions else positions[p]
    return newPositions


def calc2(pos, splitters, maxY):
    currentY = pos[1]
    newPositions = {}
    newPositions[pos] = 1
    while currentY < maxY - 1:
        positions = calc_beam_locations2(newPositions, splitters)
        newPositions = {}
        for p in positions:
            newP = (p[0], p[1] + 1)
            newPositions[newP] = positions[p]
        currentY += 1

    totalTimelines = 0
    for p in newPositions:
        totalTimelines += newPositions[p]
    return totalTimelines


def solve_part1(fileInfo):
    pos, splitters, maxY = get_values(fileInfo)
    return calc(pos, splitters, maxY)


def solve_part2(fileInfo):
    pos, splitters, maxY = get_values(fileInfo)
    return calc2(pos, splitters, maxY)
