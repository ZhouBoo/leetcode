# 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        sorted_intervals = sorted(intervals, key=lambda iters: iters[0])
        # print('sorted_intervals = ', sorted_intervals)
        merge_arr = []
        merge_lenght = 0
        for (index, interval) in enumerate(sorted_intervals):
            # print("merge_arr:", merge_arr)
            if not merge_arr:
                merge_arr.append(interval)
                merge_lenght += 1
                ## 如果上一个的结尾大于现在的起始合并
            elif merge_arr[merge_lenght - 1][1] >= interval[0]:
                last = merge_arr.pop()
                last[1] = max(last[1] ,interval[1])
                merge_arr.append(last)
            else:
                merge_arr.append(interval)
                merge_lenght += 1
        return merge_arr

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,4],[2,3]]))