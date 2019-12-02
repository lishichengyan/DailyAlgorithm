# 知识点
## 什么是哈希表
From wikipedia:

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.
## 如何解决冲突
1. Seperate chaining
* 哈希表是一个链表数组，当出现冲突时，value会被插入到表头。
* pros: 容易实现
* cons: 需要额外的数据结构，新建链表节点需要时间，如果频繁出现哈希冲突，查找效率会大打折扣（退化成链表）
2. Open address hashing
```h(x) = (Hash(key) + F(i)) mod TableSize```, where ```F(0) = 0```. 
* Linear probing  
```F(i)``` is a linear function.  
* Quadratic probing
```F(i)``` is a quadratic function.  
* Double hashing
```F(i) = i*Hash2(key)```
## Rehash 
1. Load factor
```load factor = n / k```, where ```n``` is the occupied entries, ```k``` is the number of buckets. (In a good hash table, each bucket has zero or one entries, and sometimes two or three, but rarely more than that.)
2. When to rehash?
If load factor is greater than a threshold (for example load factor of HashMap in Java10 is 0.75), we extend hash table's size (usually double).
