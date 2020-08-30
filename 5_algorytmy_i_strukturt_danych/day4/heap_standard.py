from heapq import heappop, heappush


def heap_sort(data: list) -> list:
    heap = []
    for item in data:
        heappush(heap, item)
    return [heappop(heap) for _ in range(len(heap))]


if __name__ == "__main__":
    print(heap_sort([2, 6, 2, 5, 6, 7, 767, 76, 2, 54]))