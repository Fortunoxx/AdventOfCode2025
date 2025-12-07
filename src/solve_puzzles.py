"""
Advent of Code 2025 Puzzle Solver
Main entry point for solving all daily puzzles.
"""

import sys
from typing import Dict, Tuple
import importlib

# Add puzzle module to path
sys.path.append("src/puzzle")
import puzzle


# ANSI Color codes
class Colors:
    """Terminal color codes for formatted output."""

    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    TURQUOISE = "\033[36m"


class PuzzleSolver:
    """Handles solving Advent of Code puzzles."""

    def __init__(self, test_mode: bool = True):
        """
        Initialize puzzle solver.

        Args:
            test_mode: If True, use sample data. If False, use real input data.
        """
        self.test_mode = test_mode
        self.max_day = 6  # Update as more days are completed

    def get_file_info(
        self, day: int, key: str = "input", has_extra_file: bool = False
    ) -> Dict[str, str]:
        """
        Get file path information for a puzzle day.

        Args:
            day: Day number (1-25)
            key: File key identifier
            has_extra_file: Whether day has a secondary input file

        Returns:
            Dictionary with key and file path
        """
        day_str = f"{day:02d}"
        suffix = "-2" if has_extra_file else ""

        if self.test_mode:
            file_path = f"test/data/day{day_str}.sample{suffix}.dat"
        else:
            file_path = f"src/data/day{day_str}.input.dat"

        return {"key": key, "file": file_path}

    def fetch_puzzle_data(self) -> None:
        """Download puzzle input data for all days."""
        print(f"{Colors.PURPLE}\n--- Fetching puzzle data ---{Colors.RESET}\n")

        locked = False
        for day_num in range(1, 13):  # Days 1-12
            day_str = f"{day_num:02d}"
            print(f"{Colors.RESET}Day {day_str}: fetching puzzle data...")

            file_name, skipped, locked = puzzle.fetch_for_day(day_str, locked)

            status = f"{Colors.ORANGE} | skipped" if skipped else ""
            print(
                f"{Colors.RESET}Day {day_str}: {Colors.GREEN}fetching complete: {file_name}{status}"
            )

    def solve_day(self, day: int) -> Tuple[any, any]:
        """
        Solve both parts of a specific day's puzzle.

        Args:
            day: Day number to solve

        Returns:
            Tuple of (part1_result, part2_result)
        """
        try:
            day_module = importlib.import_module(f"day{day:02d}")
            file_info = self.get_file_info(day)

            part1 = day_module.solve_part1(file_info)
            part2 = day_module.solve_part2(file_info)

            return part1, part2
        except (ImportError, AttributeError) as e:
            return f"Not implemented", f"Not implemented"

    def print_result(self, day: int, part: int, result: any) -> None:
        """
        Print formatted puzzle result.

        Args:
            day: Day number
            part: Part number (1 or 2)
            result: Solution result
        """
        print(
            f"{Colors.RESET}Day {Colors.ORANGE}{day:02d}{Colors.RESET}: "
            f"Part {Colors.ORANGE}{part}{Colors.RESET}: "
            f"{Colors.GREEN}{result}"
        )

    def solve_all(self) -> None:
        """Solve all available puzzle days."""
        print(f"{Colors.PURPLE}\n--- Solving puzzles now ---{Colors.RESET}\n")

        for day in range(1, self.max_day + 1):
            try:
                part1, part2 = self.solve_day(day)
                self.print_result(day, 1, part1)
                self.print_result(day, 2, part2)
            except Exception as e:
                print(f"{Colors.RED}Day {day:02d}: Error - {e}{Colors.RESET}")


def parse_arguments() -> bool:
    """
    Parse command line arguments.

    Returns:
        Boolean indicating test mode (True) or production mode (False)
    """
    if len(sys.argv) > 1:
        test_mode = int(sys.argv[1]) != 0
    else:
        test_mode = True  # Default to test mode

    return test_mode


def main() -> None:
    """Main entry point for puzzle solver."""
    test_mode = parse_arguments()

    mode_str = "TEST" if test_mode else "PUZZLE"
    print(f"{Colors.TURQUOISE}Running in {mode_str} mode{Colors.RESET}")

    solver = PuzzleSolver(test_mode=test_mode)
    solver.fetch_puzzle_data()
    solver.solve_all()

    print(f"\n{Colors.GREEN}All puzzles complete!{Colors.RESET}\n")


if __name__ == "__main__":
    main()
