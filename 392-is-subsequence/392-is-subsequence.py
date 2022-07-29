class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '' and t != '':
            return  True

        i, j, cont = 0, 0, 0
        while True:
            if j >= len(t) or i >= len(s):
                if cont == len(s):
                    return True
                else:
                    return False 
            if t[j] == s[i]:
                i+=1
                j+=1
                cont+=1
            else:
                j+=1