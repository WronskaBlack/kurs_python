def power1(x: float, n: int) -> float:
    if n < 0:
        return power1(1/x, -n)
    result = 1
    for _ in range(n):
        result *= x
    return result


def power(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return pow(1 / x, -n)

    if n % 2 == 0:
        value = power(x, n // 2)
        return value * value
    else:
        return power(x, n - 1) * x


print(power(3, 3))
print(power1(3, -3))
