class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum, leftSum = 0, sum(nums)

        for j in range(0, len(nums)):
            leftSum -= nums[j]
            if leftSum == rightSum:
                return j
            rightSum += nums[j]
        return -1