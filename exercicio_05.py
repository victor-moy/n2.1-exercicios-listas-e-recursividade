chamadas_naive = 0
chamadas_memo = 0


def fib_naive(n):
    global chamadas_naive
    chamadas_naive += 1
    # Caso base: fib(0) = 0, fib(1) = 1
    if n <= 1:
        return n
    # Chamada recursiva: sem memoização, recalcula subproblemas repetidamente
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, cache={}):
    global chamadas_memo
    chamadas_memo += 1
    # Caso base
    if n <= 1:
        return n
    # Se já foi calculado, retorna do cache (evita recomputação)
    if n in cache:
        return cache[n]
    # Chamada recursiva: armazena resultado antes de retornar
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


# Teste com n = 20
n = 20

resultado_naive = fib_naive(n)
resultado_memo = fib_memo(n)

print(f"fib({n}) = {resultado_naive}")
print(f"Chamadas fib_naive: {chamadas_naive}")
print(f"Chamadas fib_memo:  {chamadas_memo}")
print(f"Redução de chamadas: {chamadas_naive - chamadas_memo} ({chamadas_naive // chamadas_memo}x menos)")