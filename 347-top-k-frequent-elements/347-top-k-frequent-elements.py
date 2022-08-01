class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        sortedMap = sorted(hashmap, key=hashmap.get, reverse=True)
        x = 0
        solution = []

        while x != k:
            solution.insert(x, sortedMap.pop(0))
            x+=1

        return solution