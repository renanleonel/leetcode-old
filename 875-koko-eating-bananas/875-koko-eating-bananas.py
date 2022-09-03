import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        local = right

        while left <= right:
            speed = (left+right)//2
            hours = 0

            for i in piles:
                hours += math.ceil(i/speed)

            if hours > h:
                left = speed + 1
                
            else:
                local = min(local, speed)
                right = speed - 1

        return local