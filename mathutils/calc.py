def add(a, b):
    return a + b
    return 2


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial requires a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci requires a non-negative integer")
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
