class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        sortedMap = sorted(hashmap, key=hashmap.get)
        return sortedMap.pop(0)