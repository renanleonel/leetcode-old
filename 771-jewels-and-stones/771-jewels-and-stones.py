class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for jewel in jewels:
            for i in range(len(stones)):
                if jewel == stones[i]:
                    ans+=1
                    
        return ans