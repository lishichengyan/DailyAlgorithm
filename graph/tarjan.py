"""
参见：https://www.cnblogs.com/nullzx/archive/2017/12/04/7968110.html
重点是要理解dfn和low数组：
1) dfn[u]是访问节点u的时间戳，因此，对于u的任意子节点v，总是有dfn[u] > dfn[v]
2) 如果v的父亲是u，low[v]的含义是从v不经过u访问到祖先节点的最小时间戳

那么，如果low[v] > dfn[u]，这就意味着，如果v能不经过u访问到自己的祖先，则这个祖先应该是u的孩子（因为时间戳比u大），显然矛盾！
也就是说，v要访问自己的祖先必定要经过u，因此，uv必然是割边。
而对于割点，这个条件可以放宽为low[v] >= dfn[u]，因为存在最后一个点是割点的情况，例如：
 1
  \
   2
    \
     3
从1开始深度优先搜索，3的low和dfn都是3，3是一个割点。

"""

# 找割边（无向图）
# 找割点（无向图）
"""
private void dfs0(int v){
    dfn[v] = low[v] = ++visitOrder;  # 打时间戳
    for(Edge e : ug.adj[v]){  # 遍历以v为起点的每条边e
        int w = e.to();  # w是v的孩子
        if(!marked[w]){  # 如果w没有被访问过
            marked[w] = true;  # 访问它
            parent[w] = v;  # 记录父子关系
            dfs0(w);  # 深搜
            low[v] = Math.min(low[v], low[w]);  # 从深搜中返回后，更新low[v],，这一步的意思是，如果v的儿子w能够不通过v就访问到祖先，那么v也能不通过父顶点访问到祖先

            /*判断割点*/
            if(low[w] >= dfn[v]){
                isCutVer[v] = true;  # v为割点
                /*判断桥*/
                if(low[w] > dfn[v]){
                    listE.add(new int[]{v, w});  # vw为桥
                }
            }
        }else if(parent[v] != w && dfn[w] < dfn[v]){  # 如果w已经被访问过，并且v的父亲也不是w，说明w是v可以不通过父亲访问到的祖先，所以要更新v的low
            low[v] = Math.min(low[v], dfn[w]);
        }
    }
}
"""

# 例题：1192. Critical Connections in a Network
class Solution:
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g = collections.defaultdict(list)
        for c in connections:
            g[c[0]].append(c[1])
            g[c[1]].append(c[0])
        
        dfn, low = [0]*n, [0]*n
        vis, par = [0]*n, [-1]*n
        tag = 0
        res = []
        
        def tarjan(v):
            nonlocal tag
            tag = tag + 1
            dfn[v] = tag
            low[v] = tag
            
            for w in g[v]:
                if not vis[w]:
                    vis[w] = 1
                    par[w] = v
                    tarjan(w)
                    low[v] = min(low[v], low[w])
                    
                    if low[w] > dfn[v]:
                        res.append([v, w])
                elif par[v] != w and dfn[w] < dfn[v]:
                    low[v] = min(low[v], dfn[w])
        
        for i in range(n):
            tarjan(i)
            
        return res

# 找SCC（有向图）
