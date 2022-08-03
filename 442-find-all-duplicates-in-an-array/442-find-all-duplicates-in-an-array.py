class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        ans = []
        for index, number in enumerate(nums):
            duplicate = number
            if duplicate in hashmap:
                ans.append(duplicate)
            hashmap[number] = index
        return ans