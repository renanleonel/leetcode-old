class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            hashmap = {}
            substring = 0
            j = i
            for j in range(i, len(s)):
                if s[j] in hashmap:
                    break
                else:
                    substring+=1
                    longest = max(substring,longest)
                    hashmap[s[j]] = j

        return longest
            
            