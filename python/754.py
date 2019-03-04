class Solution:
    def reachNumber(self, target):
        target = abs(target)

        import math
        x1 = (-1 + math.sqrt(1 + 8 * target)) / 2
        n = int(math.ceil(x1))
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