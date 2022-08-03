class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for index, number in enumerate(nums):
            duplicate = number
            if duplicate in hashmap:
                return duplicate

            hashmap[number] = index
