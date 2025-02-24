class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans =1
        no = float(n)
        if no<0:
            no = no *(-1)
        while no !=0:
            if no%2==0:
                x = x * x
                no = no/2
            else:
                ans = ans * x
                no = no - 1
        if n<0:
            ans = 1.0/ans
        return ans

        