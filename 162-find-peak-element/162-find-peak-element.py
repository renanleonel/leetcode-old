class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
            
        while start <= end-1:
            mid = (start+end)//2
            
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            
            elif nums[mid] < nums[mid-1]:
                end = mid - 1
            
            else:
                return mid
            
        if nums[start] >= nums[end]:
            return start
        else:
            return end