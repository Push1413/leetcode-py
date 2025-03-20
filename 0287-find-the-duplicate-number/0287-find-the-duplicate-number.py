class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==curr:
                return curr
            curr = nums[i]

        