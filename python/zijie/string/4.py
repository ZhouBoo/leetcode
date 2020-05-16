# 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"

import functools

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul_matrix = []
        reversed_num1 = [int(x) for x in reversed(num1)]
        for (index, num) in enumerate(reversed(num2)):
            temp_mul_matrix = []
            carry = 0
            for rn in reversed_num1:
                mul = rn * int(num) + carry
                temp_mul_matrix.insert(0, mul % 10)
                carry = int(mul / 10)
            if carry != 0:
                temp_mul_matrix.insert(0, carry)
            if not mul_matrix:
                mul_matrix = temp_mul_matrix
            else:
                temp_mul_matrix.extend([0] * index)
                carry = 0
                temp_add_matrix = []
                offset = len(temp_mul_matrix) - len(mul_matrix)
                while offset > 0:
                    mul_matrix.insert(0, 0)
                    offset -= 1
                for reusult in zip(reversed(mul_matrix), reversed(temp_mul_matrix)):
                    r = reusult[0] + reusult[1] + carry
                    temp_add_matrix.insert(0, r % 10)
                    carry = int(r / 10)
                mul_matrix = temp_add_matrix
                if carry != 0:
                    mul_matrix.insert(0, carry)
        int_str = functools.reduce(lambda a, b: '%s%s' % (a, b), mul_matrix)
        return '%s' % int(int_str)



print(Solution().multiply('123', '456'))
print(Solution().multiply('2', '456'))
print(Solution().multiply('0', '456'))
print(Solution().multiply('456', '0'))
