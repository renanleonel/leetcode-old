class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {}

        for i in range(len(s)):
            if s[i] in hashmapS:
                if not hashmapS[s[i]] == t[i]:
                    return False

            if t[i] in hashmapT:
                if not hashmapT[t[i]] == s[i]:
                    return False

            hashmapS[s[i]] = t[i]
            hashmapT[t[i]] = s[i]

        return True
        