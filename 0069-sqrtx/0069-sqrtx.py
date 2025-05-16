class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low = 1
        high = x//2
        ans = 0

        while low<=high:
            mid = low + (high-low) // 2
            product = mid*mid
            if x==product:
                return mid
            elif x>product:
                low = mid+1
                ans = mid
            elif x<product:
                high = mid-1
        return ans
        