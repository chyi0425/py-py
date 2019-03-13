# coding: utf-8

class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be l.
        :type k: int
        """
        self.queue = []
        self.size = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the Operation is successful.
        :type value: int
        :rtype bool
        """
        if not self.isFull():
            self.queue.insert(0, value)
            self.rear += 1
            return True
        else:
            return False

    def insertLast(self, value):
        if not self.isFull():
            self.queue.append(value)
            self.rear += 1
            return True
        else:
            return False

    def deleteFront(self):
        if not self.isEmpty():
            self.queue.pop(0)
            self.rear -= 1
            return True
        else:
            return False

    def deleteLast(self):
        if not self.isEmpty():
            self.queue.pop()
            self.rear -= 1
            return True
        else:
            return False

    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear - 1]

    def isEmpty(self):
        return 0 == self.rear

    def isFull(self):
        return self.rear == self.size
