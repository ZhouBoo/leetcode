# LRU缓存机制
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

 

# 进阶:

# 你是否可以在 O(1) 时间复杂度内完成这两种操作？

#  示例:

# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3


class DoubleLinkNode:

    def __init__(self, key, value, next=None, prev=None):
        self.prev = prev
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.key_dict = {}
        self.capacity = capacity
        self.header = None
        self.tail = None
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.key_dict.keys():
            node = self.key_dict[key]
            self.remove_node(node)
            self.insert_node(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_dict.keys():
            node = self.key_dict[key]
            node.value = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            node = DoubleLinkNode(key, value)
            if self.count < self.capacity:
                self.insert_node(node)
            else:
                self.make_room()
                self.insert_node(node)
    
    def make_room(self):
        if self.tail is not None:
            last_node = self.tail
            last_node.prev.next = None
            self.tail = last_node.prev
            self.count -= 1
            print('make room:', last_node.key, last_node.value)
            self.key_dict.pop(last_node.key, None)
            
        
    def insert_node(self, node):
        if self.header is not None:
            node.next = self.header
            self.header.prev = node
            self.header = node
        else:
            self.header = node
            self.tail = node
        self.key_dict[node.key] = node
        self.count += 1

    def remove_node(self, node):
        if node.prev is None:
            if node.next is not None:
                self.header = None
                self.tail = None
            else:
                self.header = node.next
                node.next.prev = None
        elif node.next is None:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.count -= 1
        self.key_dict.pop(node.key, None)

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print('get: 1', obj.get(1))
obj.put(3, 3)
print('get: 2', obj.get(2))
obj.put(4, 4)
print('get: 1', obj.get(1))
print('get: 3', obj.get(3))
print('get: 4', obj.get(4))
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# obj = LRUCache(3)
# obj.put(1, 1)
# obj.put(2, 2)
# obj.put(3, 3)
# obj.put(4, 4)
# print('get: ', obj.get(4))
# print('get: ', obj.get(3))
# print('get: ', obj.get(2))
# print('get: ', obj.get(1))
# obj.put(5, 5)
# print('get: ', obj.get(1))
# print('get: ', obj.get(2))
# print('get: ', obj.get(3))
# print('get: ', obj.get(4))
# print('get: ', obj.get(5))




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# My failed cache  array version
#     def __init__(self, capacity: int):
#         self.head = 0
#         self.tail = 0
#         self.count = 0
#         self.cache = []
#         self.keyDict = {}
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key in self.keyDict.keys():
#             value = self.swap_previous(key)
#             print('cache: get', self.cache, 'dict: ', self.keyDict, self.head, self.tail)
#             return value
#         return -1

#     def swap_previous(self, key):
#         if key in self.keyDict.keys():
#             index = self.keyDict[key]
#             self.head = index + 1
#             if self.head >= self.count:
#                 self.head = 0
#             value, _ = self.cache[index]
#             # # head move to next
#             # p_index = self.head - 1
#             # if p_index < 0:
#             #     p_index = self.count - 1
#             # pValue, pKey = self.cache[p_index]
#             # self.cache[p_index] = (value, key)
#             # self.keyDict[key] = p_index
#             # self.cache[index] = pValue, pKey
#             # self.keyDict[pKey] = index
#         return value

#     def put(self, key: int, value: int) -> None:
#         if key in self.keyDict.keys():
#             ## 是否存在
#             valueIndex = self.keyDict[key]
#             _, oldKey = self.cache[valueIndex]
#             self.cache[valueIndex] = (value, key)
#             self.swap_previous(key)
#         elif self.count < self.capacity:
#             ## 如果不存在，且还没满
#             self.cache.append((value, key))
#             self.keyDict[key] = self.count
#             self.tail = self.count
#             self.count += 1
#         else:
#             ## 如果不存在，但是满了
#             _, oldKey = self.cache[self.head]
#             self.cache[self.head] = (value, key)
#             self.keyDict.pop(oldKey, None)
#             self.keyDict[key] = self.head

#             self.head += 1 
#             if self.head >= self.capacity:
#                 self.head = 0
#             self.tail += 1
#             if self.tail >= self.capacity:
#                 self.tail = 0
#         print('cache: put', self.cache, 'dict: ', self.keyDict, self.head, self.tail)

# # Your LRUCache object will be instantiated and called as such:
# [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]




# # obj = LRUCache(2)

# # print(obj.get(2))
# # obj.put(2, 6)
# # print(obj.get(1))
# # obj.put(1, 5)
# # obj.put(1, 2)
# # print(obj.get(1))
# # print(obj.get(2))

# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# ### case
# # obj.put(2, 1)
# # obj.put(3, 2)
# # print(obj.get(3))
# # print(obj.get(2))
# # obj.put(4, 3)
# # print(obj.get(2))
# # print(obj.get(3))
# # print(obj.get(4))