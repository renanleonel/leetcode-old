class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        ans = []
        for kid in candies:
            greatest = max(greatest, kid)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
        return ans