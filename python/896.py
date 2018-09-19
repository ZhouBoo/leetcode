# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direct_up = None
        last = None
        for i in A:
            if last == None:
                last = i
                continue
            else:
                is_up = i > last
                if direct_up == None:
                    if last != i:
                        direct_up = is_up
                    last = i
                elif direct_up == is_up or i == last:
                    last = i
                    continue
                else:
                    return False
        return True
            

# A = [1,2,4,5]
# A = [1,1,1]
# A = [6,5,4,4]
A = [1,1,2]
print(Solution().isMonotonic(A))