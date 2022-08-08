class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for index in range(len(s)):
            hashmap[s[index]] = 1 + hashmap.get(s[index], 0)

        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i

        return -1