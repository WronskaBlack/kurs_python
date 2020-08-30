class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f"ListNode({self.data})"
class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0
    def prepend(self, data):
        new_node = ListNode(data=data, next=self.head)
        self.head = new_node
        self._length += 1
    def append(self, data):
        if self.head is None:
            self.prepend(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data=data)
            self._length += 1
    def find(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current
    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        # Unlink from the list
        if prev is None:
            self.head = current.next
        elif current is not None:
            prev.next = current.next
            current.next = None
        self._length -= 1
    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node
    def traverse(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self._length


if __name__ == "__main__":
    linked_list = LinkedList()
    for key in range(10):
        linked_list.append(key)
        print(len(linked_list))
    print(linked_list.traverse())