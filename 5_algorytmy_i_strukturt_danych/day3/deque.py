from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, element):
        self._queue.append(element)

    def dequeue(self):
        return self._queue.popleft()

class Queue2:
    def __init__(self):
        self._in = []
        self._out = []

    def enqueue(self, element):
        self._in.append(element)

    def dequeue(self):
        if not self._out:
            for _ in range(len(self._in)):
                element = self._in.pop()
                self._out.append(element)
        return self._out.pop()

if __name__ == "__main__":
    queue = Queue2()
    for i in range(5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(10)
    print(queue.dequeue())

