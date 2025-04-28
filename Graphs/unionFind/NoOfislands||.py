def numOfIslands(rows, cols, A):
    count =0
    parent = [i for i in range(rows*cols)]
    rank = [0 for i in range(rows*cols)]
    grid = [[0 for i in range(cols)]for _ in range(rows)]
    res = []

    def find(u):
        if parent[u]!=u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u,v):
        root_u = find(u)
        root_v = find(v)

        if root_u==root_v:
            return False

        if rank[root_u]<rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_v]<rank[root_u]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u]+=1
        return True

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for x,y in A:
        if grid[x][y] == 1:
            res.append(count)
            continue

        grid[x][y]=1
        count+=1
        index1 = x*rows + y

        for dx,dy in directions:
            newRow = x+dx
            newCol = y+dy

            if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]==1:
                index2 = newRow * rows + newCol
                if union(index1,index2):
                    count-=1

        res.append(count)
    return res


if __name__=='__main__':
    n = 4
    m = 5
    A = [(1,1),(0,1),(3,3),(3,4)]
    print(numOfIslands(n,m,A))

