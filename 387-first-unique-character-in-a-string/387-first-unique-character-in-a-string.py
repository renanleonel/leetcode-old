class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for index in range(len(s)):
            hashmap[s[index]] = 1 + hashmap.get(s[index], 0)

        if 1 in hashmap.values():
            for i in range(len(s)):
                if s[i] == list(hashmap.keys())[list(hashmap.values()).index(1)]:
                    return i
        return -1