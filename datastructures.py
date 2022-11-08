class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
            
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
    
stack = Stack()
for i in range(1, 5):
    stack.push(i)
print(stack.__str__())
print(stack.pop())
print(stack.stack)
print(stack.peek())

from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.popleft()

    def __str__(self):
        return str(self.queue)

queue = Queue()
for i in range(10):
    queue.enqueue(i)

print(queue.queue)
print(queue.dequeue())
print(queue.queue)

class MaxHeap():
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            return False
        return max
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)
    
    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[index] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[index] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)

maxheap = MaxHeap([1123,1,54123,123,12,312,3,21])
print(maxheap)
maxheap.push(10)
print(maxheap)
print(maxheap.pop())
print(maxheap.peek())
