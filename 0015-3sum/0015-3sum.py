class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums = sorted(nums)
       
        for i in range(n):
            # this is too avoid duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n-1
            while left < right:
                add = nums[i] + nums[left] + nums[right]
                if add >0:
                    right-=1
                elif add < 0:
                    left +=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left +=1
                    # this is too avoid duplicate
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return ans

            


            


        