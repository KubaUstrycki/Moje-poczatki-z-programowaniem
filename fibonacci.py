def fibonacci (liczba):
    if liczba == 1:
        return [1]
    if liczba < 1:
        return []

    fib = [1,1]

    for li in range(0, liczba-2):
        fib.append(fib[li] + fib[li+1])

    return fib


print(fibonacci(6))

