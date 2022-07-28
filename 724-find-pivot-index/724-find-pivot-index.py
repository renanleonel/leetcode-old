class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = 0
        leftSum = 0
        for i in range(len(nums)):
            leftSum += nums[i]   
        for j in range(0, len(nums)):
            leftSum -= nums[j]
            if leftSum == rightSum:
                print(j)
                return j
            rightSum += nums[j]
        return -1