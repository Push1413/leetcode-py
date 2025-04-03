from functools import lru_cache

def minDistance(arr, k):
    arr.sort()

    @lru_cache
    def dp(left, right, k):
        if k==1:
            mid = arr[(left+ right) // 2]
            return sum(abs(arr[i]-mid) for i in range (left,right+1))
        else:
            return min(dp(left,i,1)+dp(i+1,right,k-1) for i in range(left,right-k +2))

    return dp(0,len(arr)-1,k)


if __name__ == '__main__':
    num = [1,4,8,10,20]
    k = 3
    print(minDistance(num,k))