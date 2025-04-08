# https://leetcode.com/problems/course-schedule/description/
def canFinish(numCourses, prerequisites):
    adjList = [[] for _ in range(numCourses)]
    visited = [False] * numCourses
    checked = [False] * numCourses

    for course, pre in prerequisites:
        # pre -> course
        adjList[pre].append(course)

    def DFS(node):
        if visited[node]:
            return False # this is for cycle detecton in current recurssion cycle
        if checked[node]:
            return True # This is for getting out of inf loop

        visited[node] = True
        for nei in adjList[node]:
            if not DFS(nei):
                return False
        visited[node]= False
        checked[node] = True
        return True

    for course in range(numCourses):
        if not checked[course]:
            if not DFS(course):
                return False

    return True


if __name__ =='__main__':
    numCourses = 3
    prerequisites = [[0, 1], [0, 2], [1, 2]]
    print(canFinish( numCourses, prerequisites))
