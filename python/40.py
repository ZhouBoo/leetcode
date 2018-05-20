
class Solution():
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        sort_nums = [x for x in candidates if x <= target]
        sort_nums.sort()

        print(len(sort_nums))
        
        temp = list()
        results = list()
        exists_set = set()

        self.generate(0, sort_nums, results, temp, exists_set, 0, target)

        return results

    def hash_array(self, nums):
        sums = 5381
        for i in nums:
            e = sums << 5
            sums = sums + e + i
        return sums
        


    def generate(self, index, nums, results, temp, exists_set, sum, target):
        nonlocal results
        """
        :type index: int
        :type nums: List[int]
        :type results: List[int]
        :type temp: List[int]
        :type exists_set: set[int]
        :type sum: int
        :type target: int
        :rtype: None
        """
        if sum > target or index >= len(nums):
            return 

        new_sum = sum + nums[index]
        temp.append(nums[index])

        hash_num = self.hash_array(temp)
        if new_sum == target and hash_num not in exists_set:
            results.append(temp)
            exists_set.add(hash_num)
            # print(results)
            print(len(results))

        self.generate(index + 1, nums, results, temp, exists_set, new_sum, target)

        new_sum -= nums[index]
        temp.pop()

        self.generate(index + 1, nums, results, temp, exists_set, new_sum, target)


s = Solution()
candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27

r = s.combinationSum2(candidates, target)
print(r)