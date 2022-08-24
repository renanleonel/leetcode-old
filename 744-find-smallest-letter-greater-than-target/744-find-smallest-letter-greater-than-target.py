class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters)-1
        while start <= end:
            middle = (start+end)//2
            if letters[middle] <= target:
                start = middle + 1
            elif letters[middle] >= target:
                end = middle - 1
            else:
                if middle == len(letters)-1:
                    return letters[0]
                else:
                    return letters[middle+1]
        if start > len(letters)-1:
            return letters[0]
        else:
            return letters[start]