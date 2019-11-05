# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
class DSU(object):
    def __init__(self):
        self.par = list(range(10001))
        self.rnk = [0] * 10001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True
    
class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # do Kruskal
        uf = DSU()
        connections.sort(key = lambda elem: elem[2])
        ans = 0
        for connection in connections:
            u, v, cost = connection
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                ans += cost
        s = set()
        for i in range(1, N+1):
            s.add(uf.find(i))
        # print(s)
        if len(s) == 1:
            return ans
        return -1
