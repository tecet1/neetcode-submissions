class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key : Node}

        # dummy nodes (always at the end)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove node from linkedlist
    def _remove(self, node:Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # add node to tail
    def _add_to_end(self, node:Node) -> None:
        last = self.tail.prev
        last.next = node
        node.next = self.tail
        node.prev = last
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_end(node)
            return None

        if len(self.cache) >= self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

        node = Node(key, value)
        self._add_to_end(node)
        self.cache[key] = node
        
