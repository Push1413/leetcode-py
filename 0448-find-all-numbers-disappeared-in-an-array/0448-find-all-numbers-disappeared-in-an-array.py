class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        map = set(nums)
        res = []

        for i in range(1,n+1):
            if i in map:
                continue
            else:
                res.append(i)
        
        return res


        