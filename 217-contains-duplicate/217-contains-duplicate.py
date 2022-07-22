class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for index, number in enumerate(nums):
            duplicate = number
            if duplicate in hashmap:
                return True

            hashmap[number] = index
        return False