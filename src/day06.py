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


def get_values_reversed(fileInfo):
    with open(fileInfo["file"]) as file:
        lines = [line.replace("\n", "") for line in file.readlines()]
        operation_line = lines[-1]
        lines.remove(operation_line)
        lines.insert(0, operation_line)

        results = []
        current = {}
        currentvalue = ""

        for x in range(0, len(lines[0])):  # dirty: assume all lines same length
            currentvalue = ""
            for idx in range(0, len(lines)):

                if idx == 0:
                    if lines[idx][x] in ["+", "*"]:
                        current = {}
                        current["operation"] = lines[idx][x]
                        current["values"] = []
                        results.append(current)
                    else:
                        current = results[-1]

                if lines[idx][x].isnumeric():
                    currentvalue += str(lines[idx][x])

            if currentvalue.isnumeric():
                current["values"].append(int(currentvalue))

    return results


def calc(input):
    items = []
    for i in input:
        if input[i]["operation"] == "+":
            sum = 0
            for val in input[i]["values"]:
                sum += val
            items.append(sum)
        elif input[i]["operation"] == "*":
            prod = 1
            for val in input[i]["values"]:
                prod *= val
            items.append(prod)

    s = 0
    for i in items:
        s += i

    return s


def calc2(input):
    items = []
    for i in input:
        if i["operation"] == "+":
            sum = 0
            for val in i["values"]:
                sum += val
            items.append(sum)
        elif i["operation"] == "*":
            prod = 1
            for val in i["values"]:
                prod *= val
            items.append(prod)

    s = 0
    for i in items:
        s += i

    return s


def solve_part1(fileInfo):
    return calc(get_values(fileInfo))


def solve_part2(fileInfo):
    lines = get_values_reversed(fileInfo)
    return calc2(lines)
