# import day12
# import day11
# import day10
# import day09
# import day08
# import day07
# import day06
import day05
import day04
import day03
import day02
import day01
import sys

sys.path.append("src/puzzle")
import puzzle

test = 1

if len(sys.argv) > 1:
    # First argument: test mode (0 or 1)
    test = int(sys.argv[1])


def getFileInfo(day, key="input", has_extra_file=False):
    suffix = ""
    if has_extra_file == True:
        suffix = "-2"
    if test == 0:
        return {"key": key, "file": f"src/data/day{day}.input.dat"}
    else:
        return {"key": key, "file": f"test/data/day{day}.sample{suffix}.dat"}


# use beautiful colors
W = "\033[0m"  # white (normal)
R = "\033[31m"  # red
G = "\033[32m"  # green
O = "\033[33m"  # orange
B = "\033[34m"  # blue
P = "\033[35m"  # purple
T = "\033[36m"  # turquoise

# download all puzzles
locked = False
for i in range(12):
    day = str(i + 1)
    if len(day) == 1:
        day = "0" + day
    print(f"{W}Day {day}: fetching puzzle data...")
    (fileName, skipped, locked) = puzzle.fetch_for_day(day, locked)
    suffix = ""
    if skipped == True:
        suffix = f"{O} | skipped{G}"
    print(f"{W}Day {day}: {G}fetching complete: {fileName}{suffix}")

print(f"{P}")
print(f"--- Solving puzzles now ---")
print(f"{G}")

print(f"{W}Day {O}01{W}: Part {O}1: {G}{day01.solve_part1(getFileInfo('01'))}")
print(f"{W}Day {O}01{W}: Part {O}2: {G}{day01.solve_part2(getFileInfo('01'))}")
print(f"{W}Day {O}02{W}: Part {O}1: {G}{day02.solve_part1(getFileInfo('02'))}")
print(f"{W}Day {O}02{W}: Part {O}2: {G}{day02.solve_part2(getFileInfo('02'))}")
print(f"{W}Day {O}03{W}: Part {O}1: {G}{day03.solve_part1(getFileInfo('03'))}")
print(f"{W}Day {O}03{W}: Part {O}2: {G}{day03.solve_part2(getFileInfo('03'))}")
print(f"{W}Day {O}04{W}: Part {O}1: {G}{day04.solve_part1(getFileInfo('04'))}")
print(f"{W}Day {O}04{W}: Part {O}2: {G}{day04.solve_part2(getFileInfo('04'))}")
print(f"{W}Day {O}05{W}: Part {O}1: {G}{day05.solve_part1(getFileInfo('05'))}")
print(f"{W}Day {O}05{W}: Part {O}2: {G}{day05.solve_part2(getFileInfo('05'))}")
# print(f"{W}Day {O}06{W}: Part {O}1: {G}{day06.solve_part1(getFileInfo('06'))}")
# print(f"{W}Day {O}06{W}: Part {O}2: {G}{day06.solve_part2(getFileInfo('06'))}")
# print(f"{W}Day {O}07{W}: Part {O}1: {G}{day07.solve_part1(getFileInfo('07'))}")
# print(f"{W}Day {O}07{W}: Part {O}2: {G}{day07.solve_part2(getFileInfo('07'))}")
# print(f"{W}Day {O}08{W}: Part {O}1: {G}{day08.solve_part1(getFileInfo('08'))}")
# print(f"{W}Day {O}08{W}: Part {O}2: {G}{day08.solve_part2(getFileInfo('08'))}")
# print(f"{W}Day {O}09{W}: Part {O}1: {G}{day09.solve_part1(getFileInfo('09'))}")
# print(f"{W}Day {O}09{W}: Part {O}2: {G}{day09.solve_part2(getFileInfo('09'))}")
# print(f"{W}Day {O}10{W}: Part {O}1: {G}{day10.solve_part1(getFileInfo('10'))}")
# print(f"{W}Day {O}10{W}: Part {O}2: {G}{day10.solve_part2(getFileInfo('10'))}")
# print(f"{W}Day {O}11{W}: Part {O}1: {G}{day11.solve_part1(getFileInfo('11'))}")
# print(f"{W}Day {O}11{W}: Part {O}2: {G}{day11.solve_part2(getFileInfo('11'))}")
# print(f"{W}Day {O}12{W}: Part {O}1: {G}{day12.solve_part1(getFileInfo('12'))}")
# print(f"{W}Day {O}12{W}: Part {O}2: {G}{day12.solve_part2(getFileInfo('12'))}")
