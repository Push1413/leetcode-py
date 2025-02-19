class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while end > start:
            mid = (start + end) // 2
            time = sum(math.ceil(i/mid) for i in piles)
            if time > h:
                start = mid +1
            else:
                end = mid
        return start






        