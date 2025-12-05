def get_values(fileInfo):
    file = open(fileInfo["file"]).readlines()
    parts = [part for part in file[0].split(',')]
    return [(int(x.split('-')[0]),int(x.split('-')[1])) for x in parts]

def calc(ranges):
    invalid = []
    for (start, end) in ranges:
        pos = start
        while pos <= end:
            s = str(pos)
            if s[:len(s)//2] == s[len(s)//2:]:
                invalid.append(pos)            
            pos += 1
    
    sum = 0
    for i in invalid:
        sum += i
    return sum


def calc2(ranges):
    invalid = []
    for (start, end) in ranges:
        pos = start
        while pos <= end:
            s = str(pos)
            for i in range(1, len(s)//2 + 1):
                if len(s) % i != 0:
                    continue # not even split
                pat = s[:i] * (len(s)//i)
                if s == pat:
                    invalid.append(pos)
                    break
            pos += 1
    
    sum = 0
    for i in invalid:
        sum += i
    return sum


def solve_part1(fileInfo):
    ranges = get_values(fileInfo)
    return calc(ranges)


def solve_part2(fileInfo):
    ranges = get_values(fileInfo)
    return calc2(ranges)