# https://leetcode.com/problems/course-schedule/discuss/359744/Python-Topological-sort

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct a graph, using adjacency list
        g = collections.defaultdict(list)
        indeg = collections.defaultdict(int)
        
        tot = numCourses
        for i in range(tot):
            indeg[i] = 0
            
        for i in range(len(prerequisites)):
            cur, pre = prerequisites[i]
            g[pre].append(cur)
            indeg[cur] += 1
            
        # then do topological sort
        q = []
        cnt = 0
        for k in indeg:
            if indeg[k] == 0:
                q.append(k)
        
        while q:
            cur = q.pop(0)
            print("course: ", cur)
            cnt += 1
            
            for vertex in g[cur]:
                indeg[vertex] -= 1
                if indeg[vertex] == 0:
                    q.append(vertex)
        
        # keep a counter during sorting, if counter < #vertices, there's a cycle
        return True if (cnt == tot) else False
