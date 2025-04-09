# hee hee
import time

# Memoization decorator
def memoize(func):
    cache = {}

    def memoized_func(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return memoized_func

# Standard Fibonacci
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

# memoized recursive fibonacci with the decorator
@memoize
def memo_recur_fibo(n):
    if n <= 1:
        return n
    else:
        return memo_recur_fibo(n - 1) + memo_recur_fibo(n - 2)

def main():
    n = 35

    print(f"Calculate Fibonacci({n}) without memoization...")
    start_time = time.time()
    result_no_memo = recur_fibo(n)
    end_time = time.time()
    print(f"Result: {result_no_memo}")
    print(f"Execution Time (with no memoization): {end_time - start_time:.4f} seconds\n")

    print(f"Calculating Fibonacci({n}) with memoization...")
    start_time = time.time()
    result_memo = memo_recur_fibo(n)
    end_time = time.time()
    print(f"Answer: {result_memo}")
    print(f"Execution Time (With Memoization): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
