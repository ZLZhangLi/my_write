class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackin = []
        self.stackout = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stackin.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.stackin and not self.stackout:
            return True
        else:
            return False
queue = MyQueue()
print(queue.push(1))
print(queue.push(2))
print(queue.peek())
print(queue.pop())
print(queue.empty())