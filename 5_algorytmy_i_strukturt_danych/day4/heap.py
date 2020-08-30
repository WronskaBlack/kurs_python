class Heap:
    def __init__(self):
        self._data = []

    @property
    def size(self):
        return len(self._data)

    @property
    def data(self):
        return self._data

    def append(self, value: int) -> None:
        self._data.append(value)
        self._siftup(self.size - 1)

    def pop(self) -> int:
        if self.size > 1:
            result = self.peak()
            self._data[0] = self._data.pop()
            self._siftdown(0)
            return result
        return self._data.pop()

    def peak(self) -> int:
        return self._data[0]

    def _siftup(self, n: int) -> None:
        while n > 0 and self._data[n] < self._data[n // 2]:
            self._data[n], self._data[n // 2] = self._data[n // 2], self._data[n]
            n //= 2

    def _siftdown(self, n: int) -> None:
        size = self.size
        while 2 * n + 1 < size:
            i_min = n
            if self._data[2 * n + 1] < self._data[i_min]:
                i_min = 2 * n + 1
            if 2 * n + 2 < size and self._data[2 * n + 2] < self._data[i_min]:
                i_min = 2 * n + 2
            if i_min == n:
                break
            self._data[n], self._data[i_min] = self._data[i_min], self._data[n]
            n = i_min


def heap_sort(data: list) -> list:
    heap = Heap()
    for item in data:
        heap.append(item)
    return [heap.pop() for _ in range(heap.size)]


if __name__ == "__main__":
    h = Heap()
    h.append(2)
    h.append(3)
    h.append(4)
    print(h.data)
    h.append(1)
    print(h.data)
    h.pop()
    print(h.data)
    print(heap_sort([2, 6, 2, 5, 6, 7, 767, 76, 2, 54]))
