# daily-algorithm
收集常用的数据结构/算法  
每个目录（已经/将要）包含以下数据结构/算法:  
## Sort  
1. 快排 (一个版本来自Prof. Weiss所著的*Data Structure and Algorithm Analysis*，一个版本来自*CLRS*，一个版本是Haskell)  
2. 选择排序  
3. 基数排序  
4. 归并排序  
5. 冒泡排序
6. 堆排序
## Search    
1. 二分查找  
2. bfs
3. dfs  
## Graph  
1. 图的表示 (邻接表和邻接矩阵)
2. Dijstra最短路径算法 (包括堆优化的Dijkstra)
3. Bellman-Ford算法
4. 拓扑排序
5. Kruskal算法
6. Prim算法  
7. 环检测算法
8. 二分图匹配，匈牙利算法
## Tree  
因为其特殊性，从Graph中单列出来  
1. 二叉树
1.1. 二叉树的表示  
1.2. 前序遍历 (递归+非递归)    
1.3. 后序遍历 (同上)   
1.4. 中序遍历 (同上)  
1.5. 层次遍历   
1.6. 求树高  
1.7. 求路径  
2. 二叉索引树 (Binary Indexed Tree)  
3. BST 
4. AVL树
5. 最大堆
6. 最小堆
7. 二项堆
8. Fibonacci堆
9. 左式堆
10. 字典树（Trie）
11. B树
12. B+树
## Union Find
1. 并查集（普通的、含smart union和路径压缩的）
## String  
1. LCS (也属于DP的问题)
## Basic
包括了一些基本的算法，如下：
1. 快速幂  
2. peasant multiplication（也叫古埃及乘法、俄罗斯乘法）  
3. long multiplication（grade-school multiplication，standard multiplication），参见目录下一个叫big integer multiplication的py文件
4. Schönhage–Strassen algorithm
5. kratsuba
6. Toom-Cook
7. FFT
8. 求中位数 (不用排序)  
9. 开根号
10. 求幂集
11. 单调栈找previous less，next less，previous larger，next larger
## Advanced Techniques  
高级技巧不是某个具体的算法，而是算法设计的技巧/思想，各目录下包含了该学习该技巧常见的例子：
### Divide and Conquer
1. maximum subarray
### Greedy
1. 活动安排问题
### Dynamic Programming
1. subset sum problem
2. LCS （参见String）
### Randomized Algorithm
1. 随机化的快排
