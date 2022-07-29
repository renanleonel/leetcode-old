class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isomorphic(s ,t):
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

        solution = []
        for word in words:
            if isomorphic(word, pattern) == True:
                solution.append(word)
        return solution
