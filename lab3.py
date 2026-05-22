class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class BiNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def put(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def get(self):
        if self.is_empty():
            return None
        
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
            
        self.size -= 1
        return data

class Stack:
    def __init__(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def push(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1

    def pull(self):
        if self.is_empty():
            return None
        
        data = self.first.data
        self.first = self.first.next
        self.size -= 1
        return data

class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first is None or self.last is None

    def Lput(self, data):
        node = BiNode(data)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first.prev = node
            self.first = node
        self.size += 1

    def Rput(self, data):
        node = BiNode(data)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node
        self.size += 1

    def Lget(self):
        if self.is_empty():
            return None
        
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        else:
            self.first.prev = None
            
        self.size -= 1
        return data

    def Rget(self):
        if self.is_empty():
            return None
        
        data = self.last.data
        self.last = self.last.prev
        if self.last is None:
            self.first = None
        else:
            self.last.next = None
            
        self.size -= 1
        return data