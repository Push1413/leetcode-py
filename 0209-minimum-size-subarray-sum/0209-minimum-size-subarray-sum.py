class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        n = len(nums)
        min_len = n+1
        l = 0
        
        for r in range(len(nums)):
            cur_sum +=nums[r]

            while cur_sum >= target:
                if r-l+1<min_len:
                    min_len = r-l+1
                cur_sum -=nums[l]
                l+=1
                
        return 0 if min_len >n  else min_len

                

            


        