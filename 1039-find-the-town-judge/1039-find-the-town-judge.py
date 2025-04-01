class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and not trust:
            return 1
        
        trustCount = [0] * (n+1)

        for t in trust:
            trustCount[t[0]] -= 1
            trustCount[t[1]] += 1
        
        for i in range(n+1):
            if trustCount[i] == n-1:
                return i
        
        return -1
        