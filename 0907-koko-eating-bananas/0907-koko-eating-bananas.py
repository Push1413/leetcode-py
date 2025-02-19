class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        start = 1
        end = maxPile

        while end > start:
            mid = (start + end) //2
            time = 0
            for i in piles:
                if i % mid != 0:
                    time += (i // mid) + 1
                else:
                    time += i // mid

            if time>h:
                start = mid +1
            else:
                end = mid
        return start
        