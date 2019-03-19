# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
# 每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
# 返回到达终点需要的最小移动次数。



class Solution:
    def reachNumber(self, target):
        target = abs(target)

        import math
        x1 = ( math.sqrt(1 + 8 * target) - 1) / 2
        # 一元二次方程的 x1 公式算出 x 是多少的时候可以接近 target
        n = int(math.ceil(x1))
        # 取整
        current_target = (1 + n) * n / 2
        next_step_above = abs(current_target - target)
        plus = 0
        if next_step_above % 2 != 0:
            plus = 1 if n % 2 == 0 else 2
            
        return plus + n

print(Solution().reachNumber(1) == 1)
print(Solution().reachNumber(3) == 2)
print(Solution().reachNumber(-2) == 3)
print(Solution().reachNumber(4) == 3)
print(Solution().reachNumber(5) == 5)