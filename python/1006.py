from math import floor

class Solution:
    def clumsy(self, N: int) -> int:
        ops = ['*', '/', '+', '-']
        op_index = 0
        caculator_minus: int = None
        caculator_sum: int = 0
        caculator: int = None
        # index = 0

        for i in range(0, N):
            number = N - i
            if caculator_minus is None:
                caculator_minus = number
                continue

            if ops[op_index] == '*':
                caculator_minus *= number
            elif ops[op_index] == '/':
                caculator_minus = floor(float(caculator_minus) / number)
            elif ops[op_index] == '+':
                caculator_sum += number
            else:
                if caculator is None:
                    caculator = caculator_minus
                else:
                    # print('%d, %d' % (caculator, caculator_minus))
                    caculator -= caculator_minus
                caculator_minus = number

            op_index += 1
            op_index = op_index % 4
        
        if caculator_minus is not None:
            if caculator is None:
                caculator = caculator_minus
            else:
                caculator -= caculator_minus
            
        caculator += caculator_sum
        
        return caculator


print(Solution().clumsy(4))
print(Solution().clumsy(10))
print(Solution().clumsy(10000))

