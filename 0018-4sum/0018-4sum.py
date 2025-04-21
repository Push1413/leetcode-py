class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, quad = [], []

        def kSum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            else:
                left = start
                right = len(nums)-1

                while left<right:
                    sum = nums[left]+ nums[right]
                    if sum==target:
                        ans.append(quad + [nums[left],nums[right]])
                        left+=1
                        right-=1

                        while left<right and nums[left]==nums[left-1]:
                            left +=1
                        while left <right and nums[right]==nums[right+1]:
                            right-=1
                    elif sum < target:
                        left+=1
                    else:
                        right-=1
        kSum(4,0,target)
        return ans

        