import pytest

from src.day01 import solve_part1, solve_part2

day = "01"


@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value=3):
    testdata = {"file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata) == expected_value


@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value=6):
    testdata = {"file": f"test/data/day{day}.sample.dat"}
    assert solve_part2(testdata) == expected_value
