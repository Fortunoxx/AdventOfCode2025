"""Benchmark for Day 02 solutions."""
import sys
import time
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import day02


def benchmark_part1(iterations=100):
    """Benchmark part 1 solution."""
    fileInfo = {"file": "src/data/day02.input.dat"}
    
    start_time = time.perf_counter()
    for _ in range(iterations):
        result = day02.solve_part1(fileInfo)
    end_time = time.perf_counter()
    
    avg_time = (end_time - start_time) / iterations
    return result, avg_time


def benchmark_part2(iterations=100):
    """Benchmark part 2 solution."""
    fileInfo = {"file": "src/data/day02.input.dat"}
    
    start_time = time.perf_counter()
    for _ in range(iterations):
        result = day02.solve_part2(fileInfo)
    end_time = time.perf_counter()
    
    avg_time = (end_time - start_time) / iterations
    return result, avg_time


if __name__ == "__main__":
    print("=" * 60)
    print("Day 02 Benchmarks")
    print("=" * 60)
    
    result1, time1 = benchmark_part1()
    print(f"Part 1: {result1}")
    print(f"Average time: {time1*1000:.3f} ms ({time1*1000000:.1f} μs)")
    
    print()
    
    result2, time2 = benchmark_part2()
    print(f"Part 2: {result2}")
    print(f"Average time: {time2*1000:.3f} ms ({time2*1000000:.1f} μs)")
    
    print()
    print(f"Total average time: {(time1+time2)*1000:.3f} ms")
    print("=" * 60)
