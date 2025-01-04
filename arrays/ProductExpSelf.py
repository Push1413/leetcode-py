def productExceptSelf(nums):
    ans = [1] * len(nums)
    n=1
    for i in range(len(nums)):
        ans[i] = n
        n = n * nums[i]

    n=1
    for i in reversed(range(len(nums))):
        ans[i] *= n
        n = n* nums[i]

    return ans




if __name__ == '__main__':
    num = [1,2,3,4]
    print(productExceptSelf(num))
