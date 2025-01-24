def canJump(nums):
    maxReach = 0

    for i in range(len(nums)):
        if i > maxReach:
            return False
        canGoTo = i + nums[i]
        maxReach = max(maxReach, canGoTo)
        if maxReach >= len(nums):
            return True
    return False


if __name__ == '__main__':
    num = [3,2,1,0,4]
    print(canJump(num))