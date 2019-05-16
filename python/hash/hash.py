
# 线性探测法。就用采用散列函数h0发现有冲突时就采用h1，
# 如果还有冲突就采用h2……其中hi(x)=[ h(x) + f(i) ] mod tableSize。 
# f(i)为i的线性函数，通常取f(i)=i

class Hash(object):

    def __init__(self, size=100):
        super().__init__()
        self.size = size
        self.table = [None for i in range(0, size)]


    def key_division(self, number):
        # 除法散列
        return number % self.size


    def set_value(self, key, value):
        hash_key = self.key_division(key)
        if not self.__position_available(hash_key):
            if self.__position_has_values(hash_key):
                self.table[hash_key].append(value)
            else:
                self.__made_position_to_list(hash_key, value)
        else:
            self.table[key] = value

    def get_value(self, key):
        hash_key = self.key_division(key)
        if self.__position_available(hash_key):
            return None
        else:
            return self.table[hash_key]

## private
    def __position_available(self, hash_key: int):
        return self.table[hash_key] is None


    def __position_has_values(self, hash_key: int):
        return self.table[hash_key] is type(list)


    def __made_position_to_list(self, hash_key: int, insert_value: int):
        self.table[hash_key] = [self.table[hash_key], insert_value]


        
    

if __name__ == "__main__":
    my_hash = Hash()
    my_hash.set_value(20, 'test')
    my_hash.set_value(20, 'test2')
    my_hash.set_value(21, 'good')

    print(my_hash.get_value(20))
    print(my_hash.get_value(21))