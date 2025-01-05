def maxSubArray(nums):
    sum =0
    res = nums[0]
    for i in nums:
        if sum <0:
            sum=0

        sum = sum +i
        res = max(sum, res)

    return res



if __name__ == '__main__':
    num = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(num))