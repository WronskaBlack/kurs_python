def hammingDistance(x: int, y: int) -> int:
    x = bin(x)[2:]
    y = bin(y)[2:]
    n = max(len(x), len(y))
    y = y.zfill(n)
    x = x.zfill(n)
    result = 0
    for i in range(n):
        if x[i] != y[i]:
            result += 1
    return result

def median(items: list) -> float:
    items.sort()
    n = len(items)
    if n % 2 == 0:
        return (items[n//2] + items[n//2 - 1]) / 2
    else:
        return items[(n - 1) // 2]

print(median([3, 1, 3, 9, 7, 8, 6]))
print(median([1, 2, 3, 4, 5, 9, 8, 6]))
# print(hammingDistance(4, 1))

