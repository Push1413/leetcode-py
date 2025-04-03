# https://leetcode.com/problems/course-schedule/description/
def canFinish(numCourses, prerequisites):
    adjList = [[] for _ in range(numCourses)]
    visited = [False] * numCourses
    checked = [False] * numCourses

    for src, dest in prerequisites:
        adjList[dest].append(src)

    def DFS(node):
        if visited[node]:
            return False
        if checked[node]:
            return True

        visited[node] = True
        for nei in adjList[node]:
            if not DFS(nei):
                return False
        visited[node]= False
        checked[node] = True
        return True

    for course in range(numCourses):
        if not DFS(course):
            return False

    return True


if __name__ =='__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    print(canFinish( numCourses, prerequisites))
