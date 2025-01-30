def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    merged=[]
    prev = intervals[0]
    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1],interval[1])
        else:
            merged.append(prev)
            prev = interval
    merged.append(prev)
    print(merged)


if __name__ == '__main__':
    intervals = [[1,4],[2,3]]
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    intervals2 = [[1,4],[1,4]]
    merge(intervals2)