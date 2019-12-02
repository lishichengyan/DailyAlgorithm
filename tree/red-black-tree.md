# 知识点
## 定义
A red–black tree is a kind of self-balancing binary search tree in computer science.
## 性质
1. Each node is either red or black.
2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
3. All leaves (NIL) are black.
4. If a node is red, then both its children are black.
5. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
## Application
1. set and map in C++
2. Completely Fair Scheudler in Linux Kernel
