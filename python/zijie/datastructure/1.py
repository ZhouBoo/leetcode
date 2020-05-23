# 1最小栈
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
#  示例:

# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# 输出：
# [null,null,null,null,-3,null,0,-2]

# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.sortArr = []
        self.count = 0

    def push(self, x: int) -> None:
        self.count += 1
        self.stack.append(x)
        self._sort(x)

    def pop(self) -> None:
        if not self._isEmpty():
            last = self.stack.pop()
            # print('last: ', last)
            self._removeSort(last)
            self.count -= 1
 
    def top(self) -> int:
        if self._isEmpty():
            return None
        return self.stack[self.count - 1]

    def getMin(self) -> int:
        if self._isEmpty():
            return None
        return self.sortArr[0]

    def _isEmpty(self) -> bool:
        return self.count == 0
        
    def _sort(self, x: int):
        insert_index = -1
        for (index, sa) in enumerate(self.sortArr):
            if sa >= x:
                insert_index = index
                break
        # print("insert_index:", insert_index, self.sortArr)
        if insert_index == -1:
            self.sortArr.append(x)
            # print('append')
        else:
            self.sortArr.insert(insert_index, x)
        print(self.sortArr)
    
    def _removeSort(self, x):
        self.sortArr.remove(x)





# Your MinStack #object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(-1)
obj.push(4)
obj.push(-3)
obj.pop()
obj.pop()
obj.pop()
obj.push(-100)
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3, param_4)