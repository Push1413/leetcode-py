import heapq
from collections import defaultdict
def networkDelayTime(times, n, k):
    adj_list = defaultdict(list)

    for u,v,w in times:
        adj_list[u].append((v,w))

    visit = set()
    heap = [(0, k)]

    while heap:
        time, node = heapq.heappop(heap)
        visit.add(node)

        if len(visit)==n:
            return time

        for time2,node2 in adj_list[node]:
            if node2 not in visit:
                heapq.heappush(heap,(time2+time,node2))

    return -1

if __name__=='__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print(networkDelayTime(times, n, k))
