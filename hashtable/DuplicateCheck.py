def containsDuplicate(nums):
    nums.sort()
    temp = -1
    for i in nums:
        if i==temp:
            return True
        else:
            temp = i
    return False

if __name__ == '__main__':
    num = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(num))
