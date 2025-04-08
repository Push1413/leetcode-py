# Also known as Khan's Algo
# https://leetcode.com/problems/course-schedule/description/
from collections import deque
def canFinish(numCourses, prerequisites):
    adjList = [[] for i in range(numCourses)]
    inDegree = [0] * numCourses

    for src, dest in prerequisites:
        # dest -> src
        adjList[dest].append(src)
        inDegree[src] +=1

    q = deque([i for i in inDegree if i==0])
    count =0

    while q:
        course = q.popleft()
        count +=1

        for nei in adjList[course]:
            inDegree[nei] -=1
            if inDegree[nei] == 0:
                q.append(nei)

    return count == numCourses

if __name__ =='__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    # 0 -> 1
    # for 0 indegree is zero. for 1 indgree is 1 as 0 must be completed and then u can do 1
    print(canFinish( numCourses, prerequisites))







