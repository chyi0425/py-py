def fib(n):
    """Compute the nth Fibonacci number, for n>=2."""
    pre, curr = 0, 1
    k = 2
    while k < n:
        pre, curr = curr, pre+curr
        k = k+1
    return curr

if __name__ == "__main__":
    print(fib(8))