def search(data: list, element: int) -> int:
    left, right = 0, len(data) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if data[middle] == element:
            return middle
        if data[middle] < element:
            left = middle + 1
        else:
            right = middle - 1
    return None

if __name__ == '__main__':
    print(search([1, 2, 4, 8], 4))
    print(search([1, 2, 4, 8], 9))
    print(search([1, 2, 4, 8, 10], 1))
