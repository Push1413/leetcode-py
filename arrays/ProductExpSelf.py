def productExceptSelf(nums):
    ans = []
    n=1
    for i in nums:
        ans[i] = n
        n = n * nums[i]

    n=1
    for i in reversed(nums):
        




if __name__ == '__main__':
    num = [1,2,3,4]
    print(productExceptSelf(num))
