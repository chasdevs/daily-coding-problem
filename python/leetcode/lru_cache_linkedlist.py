class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    capacity: int
    cache: dict
    head: Node
    tail: Node
    
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        print(f'get {key}')
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._add(n)
            self._print()
            return n.val
        else:
            self._print()
            return -1

    def put(self, key: int, value: int) -> None:
        print(f'put {key}')
        if key in self.cache:
            old = self.cache[key]
            self._remove(old)
            
        n = Node(key, value)
        self.cache[key] = n
        self._add(n)
        
        if len(self.cache) > self.capacity:
            del self.cache[self.tail.key]
            self._remove(self.tail)
        
        self._print()
        
    # p (n) x
    def _remove(self, n: Node):
        p = n.prev
        x = n.next
        
        if p and x:
            p.next = x
            x.prev = p
        elif p:
            p.next = None
            self.head = p
        elif x:
            x.prev = None
            self.tail = x

    # p [n]
    def _add(self, n: Node):
        if self.head:
            self.head.next = n
            n.prev = self.head
            
        self.head = n
        self.head.next = None
        
        if not self.tail:
            self.tail = self.head
            self.tail.prev = None
        
        
    def _print(self):
        keys = []
        it = self.tail
        while it.next is not None and it != self.head:
            keys.append(it.key)
            it = it.next
        keys.append(self.head.key)
        print(keys)
        print(f'head: {self.head.prev.key if self.head.prev else None} -> {self.head.key} -> {self.head.next.key if self.head.next else None}')
        print(f'tail: {self.tail.prev.key if self.tail.prev else None} -> {self.tail.key} -> {self.tail.next.key if self.tail.next else None}')


c = LRUCache(3)
c.put(1,1)
c.put(2,2)
c.put(3,3)
c.put(4,4)
r = c.get(1)
r = c.get(2)
r = c.get(4)
print(r)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# put:
#   push the item into the cache
#     if key is in cache, remove the item and add it
#     if cache is full, remove the last item in the cache (the tail)
#     if cache is not full, add item to the front

#   get item from cache
#     if item in cache, remove and add it
#     if item not in cache, return -1


# init:  []
# put 1: [1]
# put 2: [2, 1]
# get 1: [1, 2] # removed 1 and added it
# put 3: [3, 1] # removed tail
# get 2: [3, 1]
# put 4: [4, 3]
# get 1: [4, 3]
# get 3: [3, 4]

# [1, 2, 3, 4, 5]
# get 3: [3]
