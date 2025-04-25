def findBuildings(heights):
    n = len(heights)
    i = n-1
    maxHeight = 0
    ans = []

    while i>=0:
        currheight = heights[i]
        if currheight>maxHeight:
            maxHeight = currheight
            ans.append(i)
        i-=1
    return sorted(ans)

if __name__=='__main__':
    heights = [4,2,3,1]
    print(findBuildings(heights))
