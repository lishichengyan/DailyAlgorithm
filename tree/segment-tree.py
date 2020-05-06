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
