from collections import deque
class MaxQueue:
    def __init__(self):
        self.nums = []
        self.maxs = deque()
        self.cnt = 0 # 元素个数
        
    def push(self, x):
        self.nums.append(x)
        while len(self.maxs) and self.maxs[-1] < x:
            self.maxs.pop()
        self.maxs.append(x)
        self.cnt += 1
    
    def pop(self):
        if self.nums[0] == self.maxs[0]:
            self.maxs.popleft()
        self.nums.pop(0)
        self.cnt -= 1
        
    def get_max(self):
        return self.maxs[0]
    
    def get_size(self):
        return self.cnt
