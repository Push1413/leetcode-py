import heapq
from collections import defaultdict
def MSTPrimsAlgo(n,adj):
    sum =0
    visited = [0] * n
    result = []
    # weight, destNode, parentNode
    heap = [(0,0,-1)]

    while heap:
        w,n,p = heapq.heappop(heap)
        if not visited[n]:
            visited[n] = 1
            sum +=w
            if p!=-1:
                result.append([p,n])
            for n2, w2 in adj[n]:
                heapq.heappush(heap,(w2,n2,n))
    print(sum)
    return result

if __name__=='__main__':
    n = 5
    adj = defaultdict(list)
    #srcNode:[(destNode,weight)]
    adj[0].append((1,2))
    adj[0].append((2,1))
    adj[1].append((0,2))
    adj[1].append((2,1))
    adj[2].append((0,1))
    adj[2].append((1,1))
    adj[2].append((4,2))
    adj[2].append((3,2))
    adj[3].append((4,1))
    adj[3].append((2,2))
    adj[4].append((2,2))
    adj[4].append((3,1))
    print(MSTPrimsAlgo(n,adj))
