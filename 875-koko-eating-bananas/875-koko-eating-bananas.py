import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximo = max(piles)
        hours = 0
        minimoPossivel, maximoImpossivel = 0, 0

        while True:
            for i in piles:
                hours += math.ceil(i/maximo)

            if hours <= h:
                minimoPossivel = maximo
                maximo = (maximo + maximoImpossivel)//2

            else:
                maximoImpossivel = maximo
                maximo = (maximo + minimoPossivel)//2 

            if minimoPossivel == maximoImpossivel+1:
                return minimoPossivel

            hours = 0