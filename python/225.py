"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

"""
class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if x:
            self.stack.append(x)
    #     que.add(x);
    # for(int i=0; i<que.size()-1; i++) {
    #     que.add(que.poll());
    # }

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.stack:
            return None
        else:
            return self.stack.pop()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """

        return None if not self.stack else self.stack[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.stack


# Your MyStack object will be instantiated and called as such:
# x = 1
# x = ["MyStack","push","top"]

obj = MyStack()
obj.push(1)
obj.push(2)
# obj.push(None)
# param_2 = obj.pop()
# print(param_2)
print('----')
param_3 = obj.top()
print(param_3)

param_2 = obj.pop()
print(param_2)
param_5 = obj.pop()
print(param_5)
param_4 = obj.empty()
print(param_4)