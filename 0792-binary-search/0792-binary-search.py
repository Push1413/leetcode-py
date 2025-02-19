class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        if end == start:
            if nums[0]== target:
                return 0
            else:
                return -1
        else:
            while (start<= end):
                mid = (start + end) // 2
                if (target < nums[mid]):
                    end = mid-1
                elif (target > nums[mid]):
                    start = mid+1
                elif (nums[mid]== target):
                    return mid
            return -1


        
        