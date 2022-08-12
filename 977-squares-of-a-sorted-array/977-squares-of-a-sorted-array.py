class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        left, right, index = 0, len(nums)-1, len(nums)-1

        for i in range(len(nums)):
            nums[i]*=nums[i]

        while left <= right:
            if nums[right] > nums[left]:
                ans[index] = nums[right]
                right-=1
                index-=1
            else:
                ans[index] = nums[left]
                left+=1
                index-=1
        return ans