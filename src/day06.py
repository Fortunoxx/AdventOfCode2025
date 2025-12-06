def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        res = {}
        for line in file:
            while "  " in line:
                line = line.replace("  ", " ")

            parts = line.strip().split(" ")
            for idx in range(0, len(parts)):
                itm = res[idx] if idx in res else {}
                res[idx] = itm
                vals = itm["values"] if "values" in itm else []
                itm["values"] = vals

                if parts[idx].isnumeric():
                    vals.append(int(parts[idx]))
                else:
                    itm["operation"] = parts[idx]
        return res


def calc(input):
    items = []
    for i in input:
        if input[i]["operation"] == '+':
            sum = 0
            for val in input[i]["values"]:
                sum += val
            items.append(sum)
        elif input[i]["operation"] == '*':
            prod = 1
            for val in input[i]["values"]:
                prod *= val
            items.append(prod)

    s = 0
    for i in items:
        s+= i

    return s


def calc2(input):
    return 0
  

def solve_part1(fileInfo):
    return calc(get_values(fileInfo))


def solve_part2(fileInfo):    
    return calc(get_values(fileInfo))
