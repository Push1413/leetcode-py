class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedArray = sorted(nums)
        myMap = {}

        for i,num in enumerate(sortedArray):
            if num not in myMap:
                myMap[num] = i
        
        res = []
        for i in nums:
            res.append(myMap[i])
        
        return res

        