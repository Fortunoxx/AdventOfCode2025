"""Run all benchmark files and generate a summary report."""
import sys
import time
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import day01, day02, day03, day04, day05, day06


def run_benchmark(day_module, day_num, iterations=100):
    """Run benchmarks for a specific day."""
    fileInfo = {"file": f"src/data/day{day_num:02d}.input.dat"}
    
    # Check if input file exists
    if not Path(fileInfo["file"]).exists():
        return None, None, None
    
    try:
        # Part 1
        start = time.perf_counter()
        for _ in range(iterations):
            result1 = day_module.solve_part1(fileInfo)
        time1 = (time.perf_counter() - start) / iterations
        
        # Part 2
        start = time.perf_counter()
        for _ in range(iterations):
            result2 = day_module.solve_part2(fileInfo)
        time2 = (time.perf_counter() - start) / iterations
        
        return result1, result2, (time1, time2)
    except Exception as e:
        print(f"Error benchmarking day {day_num}: {e}")
        return None, None, None


if __name__ == "__main__":
    print("=" * 70)
    print("Advent of Code 2025 - Benchmark Summary")
    print("=" * 70)
    print()
    
    days = [
        (1, day01),
        (2, day02),
        (3, day03),
        (4, day04),
        (5, day05),
        (6, day06),
    ]
    
    total_time = 0
    results = []
    
    for day_num, day_module in days:
        result1, result2, times = run_benchmark(day_module, day_num)
        
        if times:
            time1, time2 = times
            day_total = time1 + time2
            total_time += day_total
            
            results.append({
                'day': day_num,
                'part1': result1,
                'part2': result2,
                'time1': time1,
                'time2': time2,
                'total': day_total
            })
            
            print(f"Day {day_num:02d}")
            print(f"  Part 1: {result1:>15} | {time1*1000:>8.3f} ms")
            print(f"  Part 2: {result2:>15} | {time2*1000:>8.3f} ms")
            print(f"  Total:  {' '*15} | {day_total*1000:>8.3f} ms")
            print()
    
    print("=" * 70)
    print(f"Total time for all solutions: {total_time*1000:.3f} ms ({total_time:.6f} s)")
    print("=" * 70)
    
    # Find slowest day
    if results:
        slowest = max(results, key=lambda x: x['total'])
        print(f"\nSlowest day: Day {slowest['day']:02d} ({slowest['total']*1000:.3f} ms)")
        
        fastest = min(results, key=lambda x: x['total'])
        print(f"Fastest day: Day {fastest['day']:02d} ({fastest['total']*1000:.3f} ms)")
