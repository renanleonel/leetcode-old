class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch for ch in s if ch.isalnum()]).lower()
        j = len(s)-1
        if s == '':
            return True
        for i in range(int((len(s)-1)/2)+1):
            if s[i] == s[j]:
                j-=1
            else:
                return False
        return True