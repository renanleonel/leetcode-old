class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maior = 0
        for num in nums:
            if (num-1) not in nums:
                tamanho = 1
                while (num+tamanho) in nums:
                    tamanho+=1

                if tamanho > maior:
                    maior=tamanho
        return maior