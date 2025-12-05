def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        banks = []
        for line in file:
            bank = []
            for char in line.strip():
                bank.append(int(char))
            banks.append(bank)
        return banks


def calc(banks, battery_count = 2):
    results = []
    for bank in banks:
        ints = []
        for pos in range(battery_count, 0, -1):
            max = 0
            mPos = 0
            for b in range(0, len(bank) - pos + 1):
                if bank[b] > max and b not in ints and b > (ints[-1] if len(ints) > 0 else -1):
                    max = bank[b]
                    mPos = b
            ints.append(mPos)

        res = 0
        for i in range(0, len(ints), 1):
            res += bank[ints[i]] * (10 ** (len(ints) - i - 1))
        results.append(res)
    return sum(results)


def calc2(banks):
    return 0


def solve_part1(fileInfo):
    banks = get_values(fileInfo)
    return calc(banks)


def solve_part2(fileInfo):
    ranges = get_values(fileInfo)
    return calc2(ranges)