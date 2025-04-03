class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ##BFS 
        graph = [[] for _ in range(numCourses)]
        inorder = [0] * numCourses

        for node, prerequisite in prerequisites:
            graph[prerequisite].append(node)
            inorder[node] +=1
        
        q = deque([i for i in range(numCourses) if inorder[i]==0])
        count = 0

        while q:
            course = q.popleft()
            count +=1

            for nei in graph[course]:
                inorder[nei] -=1
                if inorder[nei] ==0:
                    q.append(nei)

        return count==numCourses




        
        