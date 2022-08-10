class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller=0
        ans=[]
        for num in nums:
            for num2 in nums:
                if num2 < num:
                    smaller+=1
            ans.append(smaller)
            smaller = 0
        return ans