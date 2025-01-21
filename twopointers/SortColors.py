#75
def sortColors(nums):
    l,r,i= 0, len(nums)-1,0
    while i<=r:
        if nums[i]==0:
            nums[i], nums[l] = nums[l], nums[i]
            l+=1
            i+=1
        elif nums[i]==1:
            i+=1
        else:
            nums[i], nums[r] = nums[r], nums[i]
            r-=1


if __name__ == '__main__':
    nums = [0,2,1]
    sortColors(nums)
    print(nums)

