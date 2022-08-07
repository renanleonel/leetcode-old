class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maximum, containerLines = 0, len(height)-1, 0, len(height)-1
    
        while left < right:
            local = min(height[left], height[right]) * containerLines
            maximum = max(maximum, local)

            if height[left] < height[right]:
                left+=1
                containerLines-=1
            else:
                right-=1
                containerLines-=1

        return maximum