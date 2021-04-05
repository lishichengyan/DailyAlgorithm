class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = nums[:]
        m = len(self.arr)
        self.tree = [0] * (4*m+1)
        self.__build(1, 0, m-1)
        
    def __build(self, pos, low, high):
        """
        pos: root of current subtree
        low: lower bound, inclusive
        high: upper bound, inclusive
        """
        if low > high:
            return
        if low == high:
            self.tree[pos] = self.arr[low]
            return
        mid = (low + high) // 2
        self.__build(2*pos, low, mid)
        self.__build(2*pos+1, mid+1, high)
        self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]
        
    def __query(self, pos, i, j, low, high):
        """
        i: lower bound of the query, inclusive
        j: upper bound of the query, inclusive
        """
        if i <= low and j >= high:
            return self.tree[pos]
        if i > high or j < low:
            return 0
        mid = (low + high) // 2
        return self.__query(2*pos, i, j, low, mid) + self.__query(2*pos+1, i, j, mid+1, high)
    
    def __update(self, i, new_val, low, high, pos):
        """
        i: which position to update
        """
        if i < low or i > high:
            return
        if low == high:
            self.tree[pos] = new_val
            self.arr[i] = new_val
            return
        mid = (low + high) // 2
        self.__update(i, new_val, low, mid, 2*pos)
        self.__update(i, new_val, mid+1, high, 2*pos+1)
        self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]

    def update(self, i: int, val: int) -> None:
        return self.__update(i, val, 0, len(self.arr)-1, 1)

    def sumRange(self, i: int, j: int) -> int:
        return self.__query(1, i, j, 0, len(self.arr)-1)
      
class SegmentTree:
  IMAX = float("inf")

  def __init__(self, arr):
    m = len(arr)
    self.N = m  # original arr length
    self.arr = arr  # original arr
    while (m & (m-1)) != 0:
      m += 1
    self.tree = [SegmentTree.IMAX] * (2*m-1);
    self.__build(arr, 0, 0, len(arr)-1)
  
  def __build(self, arr, pos, low, high):
    """
    -1 3 0 2
    =>
       -1
      /   \
     -1    0
     / \  / \
    -1  3 0  2

    -1 -1 0 -1 3 0 2
    """
    if low == high:
      self.tree[pos] = arr[low]
      return
    mid = (low + high) // 2
    self.__build(arr, 2*pos+1, low, mid)  # left subtree
    self.__build(arr, 2*pos+2, mid+1, high)  # right substree
    self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])

  def __query(self, i, j, low, high, pos):
    if i <= low and j >= high:
      # total overlap
      return self.tree[pos]
    if i > high or j < low:
      # no overlap
      return SegmentTree.IMAX
    mid = (low + high) // 2
    return min(self.__query(i, j, low, mid, 2*pos+1), self.__query(i, j, mid+1, high, 2*pos+2))

  def __update(self, low, high, pos, i, new_val):
    """
    without lazy propagation
    """
    if low == high:
      self.tree[pos] = new_val
      self.arr[i] = new_val
    else:
      mid = (low + high) // 2
      if low <= i <= mid:
        self.__update(low, mid, 2*pos+1, i, new_val)
      else:
        self.__update(mid+1, high, 2*pos+2, i, new_val)
      
      self.tree[pos] = min(self.tree[2*pos+1], self.tree[2*pos+2])

  def printTreeArray(self):
    print(self.tree)

  def printOriginalArray(self):
    print(self.arr)

  def query(self, i, j):
    return self.__query(i, j, 0, self.N-1, 0)
  
  def update(self, i, new_val):
    # print("hi")
    self.__update(0, self.N-1, 0, i, new_val)



arr = [-1, 3, 0, 2]
segtree = SegmentTree(arr)
segtree.printTreeArray()
print(segtree.query(0, 2))
print(segtree.query(0, 1))
print(segtree.query(0, 3))
print(segtree.query(0, 0))
print(segtree.query(1, 3))
print(segtree.query(2, 3))
print(segtree.query(3, 3))
segtree.update(3,3)
segtree.printTreeArray()
segtree.printOriginalArray()
