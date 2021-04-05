class DLLNode:
    def __init__(self, key, val, pre, next):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.d = collections.defaultdict(DLLNode)
        self.head = DLLNode(-1, -1, None, None)
        self.tail = DLLNode(-1, -1, None, None)
        
        # dummy nodes
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def __unlink(self, node) -> None:
        """
        unlink the node
        
        eg. 1 <-> 2 <-> 3, unlink(2) =>  1 <-> 3
        """
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
    
    def __link(self, src_node, dest_node) -> None:
        """
        link src behind dest
        eg. 1 <-> 2 <-> 3, link(4, 2) =>  1 <-> 2 <-> 4 <-> 3
        """
        cur_head = dest_node.next
        src_node.next = cur_head
        cur_head.pre = src_node
        dest_node.next = src_node
        src_node.pre = dest_node
    
    def get(self, key: int) -> int:
        this_val = -1
        if key in self.d:
            this_node = self.d[key]
            this_val = this_node.val
            self.__unlink(this_node)
            self.__link(this_node, self.head)
        return this_val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            """
            更新node的值，unlink这个node，将它link到head之后
            """
            this_node = self.d[key]
            this_node.val = value
            self.__unlink(this_node)
            self.__link(this_node, self.head)
        else:
            if self.size + 1 > self.capacity:
                """
                丢弃dummy tail前的第一个node，然后创建新node，link到dummy head后
                """
                old_node = self.tail.pre
                old_key = old_node.key
                
                self.__unlink(old_node)
                del self.d[old_key]
                
                new_node = DLLNode(key, value, None, None)
                self.__link(new_node, self.head)
                self.d[key] = new_node
            else:
                """
                创建一个新node，link到dummy head后
                """
                self.size += 1
                new_node = DLLNode(key, value, None, None)
                self.__link(new_node, self.head)
                self.d[key] = new_node
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
