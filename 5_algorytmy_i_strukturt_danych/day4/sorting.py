import random

def bubble(data: list) -> list:
    sweep = True
    n = 1
    while sweep:
        sweep = False
        for i in range(len(data) - n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                sweep = True
        n += 1
    return data


def insertion(data: list) -> list:
    for j in range(len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = key
    return data


def merge(list1: list, list2: list) -> list:
    if not len(list1):
        return list2
    if not len(list2):
        return list1
    result = []
    size1, size2 = len(list1), len(list2)
    i, j = 0, 0
    while i < size1 and j < size2:
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < size1:
        result.append(list1[i])
        i += 1
    while j < size2:
        result.append(list2[j])
        j += 1
    return result


def divide(data: list) -> tuple:
    size = len(data)
    return data[:size // 2], data[size // 2:]


def merge_sort(data) -> list:
    if not data or len(data) == 1:
        return data
    left, right = divide(data)
    return merge(merge_sort(left), merge_sort(right))


def quick_sort(data: list, left: int, right: int) -> list:
    if left >= right:
        return data
    pivot = data[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
    quick_sort(data, left, j)
    quick_sort(data, i, right)
    return data


def counting_sort(data:list) -> list:
    counter = (max(data) + 1) * [0]
    for value in data:
        counter[value] += 1
    i = 0
    for idx, freq in enumerate(counter):
        for _ in range(freq):
            data[i] = idx
            i += 1
    return data


def counting_sort2(data:list, min: int, max: int) -> list:
    counter = (max - min + 1) * [0]
    for value in data:
        counter[value - min] += 1
    i = 0
    for idx, freq in enumerate(counter):
        for _ in range(freq):
            data[i] = idx + min
            i += 1
    return data


def selection(data: list) -> list:
    for pos in range(len(data)):
        min_idx = pos
        for i in range(pos + 1, len(data)):
            if data[i] < data[min_idx]:
                min_idx = i
        data[pos], data[min_idx] = data[min_idx], data[pos]
    return data


if __name__ == "__main__":
    data = [54, 32, 1, 4235, 43, 12, 3213, 23, 65, 21, 567, 1]
    expected = sorted(data)
    result = bubble(data)
    assert result == expected
    result = insertion(data)
    assert result == expected
    result = merge_sort(data)
    assert result == expected
    result = quick_sort(data, 0, len(data)-1)
    assert result == expected
    result = counting_sort(data)
    assert result == expected
    # print(counting_sort2([1000, 1002, 1000, 1000, 1004, 1005, 1005, 1004, 1002], 1000, 1005))
    result = selection(data)
    assert result == expected