class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    pairs+=1
        return pairs