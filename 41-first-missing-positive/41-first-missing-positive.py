class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        hashmap = {}
        lastNum = nums[len(nums)-1]
        
        for index, number in enumerate(nums):
            hashmap[number] = index

        for i in range(lastNum):
            if i not in hashmap and i > 0:
                return i
            
        if lastNum > 0:
            return lastNum+1
        else:
            return 1