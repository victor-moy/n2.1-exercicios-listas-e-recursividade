def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    print(fatorial(0))   # 1
    print(fatorial(5))   # 120
    print(fatorial(10))  # 3628800
