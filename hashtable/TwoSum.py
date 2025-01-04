def twoSum(nums, target):
    numMap ={}
    n = len(nums)

    for i in range(n):
        search = target - nums[i]
        if search in numMap:
            return [numMap[search],i]
        else:
            numMap[nums[i]]=i

    return []



if __name__ == '__main__':
    num = [3,2,4]
    print(twoSum(num,0))


