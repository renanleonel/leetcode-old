class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        
        return [left, right]
        
    def binarySearch(self, nums, target, searchingLeft):
        start, end = 0, len(nums)-1
        index = -1
        while start <= end:
            mid = (start+end)//2

            if nums[mid] == target:
                index = mid

                if searchingLeft:
                    end = mid - 1
                else: 
                    start = mid + 1

            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return index