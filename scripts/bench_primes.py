import time
from llm_benchmark.algorithms.primes import Primes


def bench(func, *args, repeat=5, warmup=1):
    for _ in range(warmup):
        func(*args)
    tmin = float("inf")
    for _ in range(repeat):
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        tmin = min(tmin, t1 - t0)
    return tmin


def main():
    cases = [
        (Primes.is_prime, 10**6 + 3),
        (Primes.sum_primes, 10**5),
        (Primes.prime_factors, 9876543210),
    ]
    for fn, arg in cases:
        dt = bench(fn, arg)
        print(f"{fn.__name__}({arg}): {dt*1000:.2f} ms")


if __name__ == "__main__":
    main()
