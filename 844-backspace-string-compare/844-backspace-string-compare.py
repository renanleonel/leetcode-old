class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        rightS, rightT = len(s)-1, len(t)-1
        skipS, skipT = 0, 0

        while rightS >= 0 or rightT >=0:
            while rightS >= 0:
                if s[rightS] == "#" :
                    skipS += 1
                    rightS-=1

                elif skipS > 0:
                    skipS -= 1
                    rightS-=1

                else:
                    break

            while rightT >= 0:
                if t[rightT] == "#" :
                    skipT += 1
                    rightT-=1

                elif skipT > 0:
                    skipT -= 1
                    rightT-=1

                else:
                    break    

            if rightS>= 0 and rightT >= 0 and s[rightS] != t[rightT]:
                return False

            if (rightS>=0) != (rightT>=0):
                return False

            rightS-=1
            rightT-=1
        return True		