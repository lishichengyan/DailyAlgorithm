class minHeap(object):
    capacity = 2
    
    def __init__(self, lst = None):
        if lst is None:
            self.__init_default()
        else:
            self.__init_from_list(lst)
            
    def __init_default(self):
        self.size = 0
        self.heap = [None] * minHeap.capacity    
    
    def __init_from_list(self, lst):
        self.heap = [None] + lst  # 不用第0个元素
        self.size = len(lst)
        self.__heapify()
        
    def __percolate_up(self, k):
        while k > 1:  # k有父亲
            parent = k // 2
            if self.heap[k] < self.heap[parent]:
                tmp = self.heap[parent]
                self.heap[parent] = self.heap[k]
                self.heap[k] = tmp
            else:
                break
            k = parent
    
    def __percolate_down(self, k):
        tmp = self.heap[k]  # 暂存当前需要调整的元素
        while 2*k <= self.size:  # 当k还有孩子
            child = 2*k  # 左孩子
            # 找最小的孩子
            if child != self.size and self.heap[child] > self.heap[child+1]:
                child += 1
            # 在k处插入更小的值
            if tmp > self.heap[child]:
                self.heap[k] = self.heap[child]
            else:
                break
            # 更新k
            k = child
        # 最后插入暂存的tmp
        self.heap[k] = tmp
    
    def __heapify(self):
        for i in range(self.size // 2, 0, -1):
            self.__percolate_down(i)
    
    def __delete_min(self):
        # lazy deletion
        if self.size == 0:
            raise IndexError("heap size is 0")
        first_val = self.heap[1]
        last_val = self.heap[self.size]
        self.size -= 1
        self.heap[1] = last_val
        self.__percolate_down(1)
        return first_val
    
    def __double_size(self):
        old = self.heap[:]
        self.heap = old + [None] * len(self.heap)
        
    def __insert(self, x):
        if self.size == len(self.heap) - 1:
            self.__double_size()
        self.size += 1
        pos = self.size
        self.heap[pos] = x
        self.__percolate_up(pos)
    
    def print_all(self):
        print("------start printing")
        print(self.heap)
        print("------end printing")
        
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.get_size() == 0
    
    def push(self, x):
        self.__insert(x)
    
    def pop(self):
        return self.__delete_min()
