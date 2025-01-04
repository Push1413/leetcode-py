def twoSum(nums, target):
    leftPointer =0
    rightPointer = len(nums) -1
    nums.sort()
    while(leftPointer<rightPointer):
        sum = nums[leftPointer]+nums[rightPointer]
        if(sum == target):
            return True
        elif(sum<target):
            leftPointer+=1
        else:
            rightPointer-=1

    return False



if __name__ == '__main__':
    num = [3,2,4]
    print(twoSum(num,6))


