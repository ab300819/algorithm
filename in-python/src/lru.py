#!/usr/bin/env python3

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._cache = {}
        self._head = Node(-1, -1)
        self._tail = Node(-1, -1)
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self._cache:
            node = Node(key, value)
            self._cache[key] = node
            self._add_to_head(node)
            self._size = self._size + 1
            if len(self._cache) > self._capacity:
                tail = self._remove_tail()
                self._cache.pop(tail.key)
                self._size = self._size - 1
        else:
            node = self._cache[key]
            node.value = value
            self._move_to_head(node)

    def _move_to_head(self, node):
        self._remove(node)
        self._add_to_head(node)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_tail(self):
        prev = self._tail.prev
        self._remove(prev)
        return prev

    def _add_to_head(self, node):
        node.next = self._head.next
        node.prev = self._head
        node.next.prev = node
        self._head.next = node


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
