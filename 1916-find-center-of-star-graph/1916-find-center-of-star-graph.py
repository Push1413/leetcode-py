class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dict = {}
        n = len(edges)
        for arr in edges:
            dict[arr[0]] = dict.get(arr[0], 0) + 1
            dict[arr[1]] = dict.get(arr[1],0) + 1
        
        for k,v in dict.items():
            if v==n:
                return k







        