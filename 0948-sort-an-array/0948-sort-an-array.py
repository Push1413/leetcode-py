class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick(nums, 0, len(nums) - 1)
        return nums

    def quick(self, nums, low, high):
        if low >= high:
            return
        
        s, e = low, high
        mid = (s + e) // 2
        pivot = nums[mid]

        while s <= e:
            while nums[s] < pivot:
                s += 1
            while nums[e] > pivot:
                e -= 1
            if s <= e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        self.quick(nums, low, e)
        self.quick(nums, s, high)