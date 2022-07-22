​can also be done with sorting, taking into consideration time complexity for sorting

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = ''.join(sorted(s))
            sortedT = ''.join(sorted(t))

            if sortedS != sortedT:
                return False
            return True
```
