# 给定两个整数 A 和 B，返回任意字符串 S，要求满足：

# S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
# 子串 'aaa' 没有出现在 S 中；
# 子串 'bbb' 没有出现在 S 中。


class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """

        (bigger, smaller) = ('a', 'b') if A > B else ('b', 'a')
        normal_patter = bigger + smaller
        bigger_patter = bigger * 2 + smaller
        min_ab = min(A, B)
        bigger_count = min(max(A, B) - min_ab, min_ab)
        normal_count = max(min_ab - bigger_count, 0)
        s = normal_patter * normal_count + bigger_patter * bigger_count + bigger * (max(A, B) - 2 * bigger_count - normal_count)
        # counter = int(max(A, B) / min(A, B))
        # first_count = min(counter, 2)
        # last_count = min((1 if counter >= 2 else 2), first_count)
        # print(first_count)
        # print(last_count)
        # insert_pattern = insert_first * first_count + insert_last * last_count
        # print(insert_pattern)
        # times = min(int((A + B) / len(insert_pattern)), min(A, B))
        # last_reset = (counter % 2) % 2
        # return insert_pattern * times + insert_first * (max(A, B) - times * first_count) + insert_last * (min(A, B) - times * last_count)
        return s


print(Solution().strWithout3a3b(3, 5))
print(Solution().strWithout3a3b(4, 10))