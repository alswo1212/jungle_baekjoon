class Node:
    def __init__(self, name):
        self.name = name
        self.pre = None
        self.next = None

    def unlink(self):
        pre, next = self.pre, self.next
        self.pre.next, self.next.pre = next, pre
        self.pre = None
        self.next = None

    def link(self, pre:"Node", next:"Node"):
        self.pre = pre
        pre.next = self
        next.pre = self
        self.next = next

class LruList:
    def __init__(self, cachesize):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next = self.tail
        self.tail.pre = self.head
        self.items = {}
        self.max_size = cachesize
        self.use_time = 0

    def add(self, node:Node):
        if node.name in self.items:
            node = self.items[node.name]
            node.unlink()
            node.link(self.head, self.head.next)
            self.use_time += 1
            return
        
        self.items[node.name] = node
        node.link(self.head, self.head.next)
        self.use_time += 5

        if len(self.items) > self.max_size:
            target = self.tail.pre
            self.items.pop(target.name)
            target.unlink()
    
def solution(cacheSize, cities):
    cache = LruList(cacheSize)
    for city in cities:
        cache.add(Node(city.lower()))
    return cache.use_time