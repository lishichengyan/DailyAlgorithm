# 知识点
## 什么是哈希表
From wikipedia:

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.
## 如何解决冲突
1. Seperate chaining
哈希表是一个链表数组，当出现冲突时，value会被插入到表头。
2. Open address hashing
2.1 Linear probing
2.2 Quadratic probing
2.2 Double hashing
## Rehash 
1
