def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        is_range_mode = True
        ranges = []
        ingredients = []

        for line in file:
            if line.strip() == "":
                is_range_mode = False
                continue
            if is_range_mode:
                parts = line.strip().split("-")
                start = int(parts[0])
                end = int(parts[1])
                ranges.append((start, end))
            else:
                ingredients.append(int(line.strip()))
        return ranges, ingredients


def calc(ranges, ingredients):
    fresh = []
    for ingredient in ingredients:
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                fresh.append(ingredient)
                break
    return fresh


def calc2(ranges):
    merged = []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    for current in sorted_ranges:
        if not merged:
            merged.append(current)
        else:
            last = merged[-1]
            if current[0] <= last[1]:  # Overlap
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)

    sum = 0
    for m in merged:
        sum += m[1] - m[0] + 1
    return sum


def solve_part1(fileInfo):
    ranges, ingredients = get_values(fileInfo)
    fresh = calc(ranges, ingredients)
    return len(fresh)


def solve_part2(fileInfo):
    ranges, _ = get_values(fileInfo)
    valid = calc2(ranges)
    return valid
