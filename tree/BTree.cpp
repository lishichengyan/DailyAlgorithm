/*
B树的定义有两种，第一种通过degree定义：
假设B树的degree是t，则：
（1）所有叶子节点都处在同一层
（2）除了根节点外，所有节点至少要有t-1个键（key），根节点最少可以只有一个键
（3）所有节点最多包含2t-1个键
（4）每个节点的孩子数等于这个节点中键的个数加1
（5）所有键都排好序

第二种通过order定义：
假设B树的order是m，则：
（1）所有叶子节点都处在同一层
（2）除了根节点外，所有节点至少要有k个键（key），根节点最少可以只有一个键，其中ceil(m/2)-1 <= k <= m-1
（3）所有节点最多包含m个键
（4）每个节点的孩子数等于这个节点中键的个数加1
（5）所有键都排好序
*/

// java实现：https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/BTree.java.html
// c++实现：https://www.geeksforgeeks.org/b-tree-set-1-introduction-2/
