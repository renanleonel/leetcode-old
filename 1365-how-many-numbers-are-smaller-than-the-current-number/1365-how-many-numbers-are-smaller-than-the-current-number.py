class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        aux = sorted(nums)
        hashmap = {}
        result = []

        for i in range(len(aux)):
            if aux[i] not in hashmap:
                hashmap[aux[i]] = i

        for i in range(len(nums)):
            result.append(hashmap[nums[i]])

        return result