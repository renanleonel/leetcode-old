class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)-1
        ans = []
        nums = sorted(nums)
        index = -1
        
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                index = mid
                
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        if index == -1:
            return []
        
        ans.append(index)
        nextIndex = index + 1

        while nextIndex <= len(nums)-1:
            if nums[nextIndex] == nums[index]:
                ans.append(nextIndex)
                nextIndex+=1
            else:
                return ans
        return ans