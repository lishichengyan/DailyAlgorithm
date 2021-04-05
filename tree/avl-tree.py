# References:
# https://blog.csdn.net/Magic1an/article/details/78881665
# https://zhuanlan.zhihu.com/p/34899732
# https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x
        self.height = 0
 

class AVLTree(object):
    def __init__(self):
         self.root = None
    
    
    # Private Methods     
    def __get_height(self, node):
        return node.height if node != None else -1
    
    
    def __get_balance_factor(self, node):
        return self.__get_height(node.left) - self.__get_height(node.right)
        
    
    def __single_rotate_with_left(self, k2):
        """
             k2             k1
            /  \           /  \
            k1  C   ===>   A  k2 
           /  \               /  \
           A   B              B   C  
        """
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = max(self.__get_height(k2.left), self.__get_height(k2.right)) + 1
        k1.height = max(self.__get_height(k1.left), k2.height) + 1 
        return k1
    
    
    def __single_rotate_with_right(self, k2):
        """
             k2             k1
            /  \           /  \
            A  k1   ===>   k2  C
              /  \        /  \
              B   C       A   B    
        """
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2
        k2.height = max(self.__get_height(k2.left), self.__get_height(k2.right)) + 1
        k1.height = max(self.__get_height(k1.right), k2.height) + 1 
        return k1
    
    
    def __double_rotate_with_left(self, k3):
        """
             k3             k2
            /  \           /  \
            k1  D   ===>   k1  K3  
           /  \           / \  / \
          A   k2         A  B  C  D
              / \
              B  C       
        """
        k3.left = self.__single_rotate_with_right(k3.left)
        return self.__single_rotate_with_left(k3)
    
        
    def __double_rotate_with_right(self, k3):
        """
             k3             k2
            /  \           /  \
            A  K1   ===>   k1  K3  
              /  \        / \  / \
             k2   D       A  B  C  D
             / \
             B  C       
        """
        k3.right = self.__single_rotate_with_left(k3.right)
        return self.__single_rotate_with_right(k3)
    
    
    def __insert(self, x, p):
        if p == None:
            p = TreeNode(x)
        elif x < p.val:
            p.left = self.__insert(x, p.left)
            if self.__get_height(p.left) - self.__get_height(p.right) == 2:
                if x < p.left.val:
                    p = self.__single_rotate_with_left(p)
                else:
                    p = self.__double_rotate_with_left(p)
        elif x > p.val:
            p.right = self.__insert(x, p.right)
            if self.__get_height(p.right) - self.__get_height(p.left) == 2:
                if x > p.right.val:
                    p = self.__single_rotate_with_right(p)
                else:
                    p = self.__double_rotate_with_right(p)
        else:
            pass
        p.height = max(self.__get_height(p.left), self.__get_height(p.right)) + 1 
        return p
    
    
    def __find_min(self, p):
        if p is None:
            return None
        else:
            if p.left is None:
                return p
            else:
                return self.__find_min(p.left)
        
    
    def __delete(self, x, p):
        # first perform normal BST deletion
        if p is None:
            return None
        elif x < p.val:
            p.left = self.__delete(x, p.left)
        elif x > p.val:
            p.right = self.__delete(x, p.right)
        else:
            if p.left is None:
                tmp = p.right
                p = None
                return tmp
            elif p.right is None:
                tmp = p.left
                p = None
                return tmp
            # p has 2 children
            min_child = self.__find_min(p.right)
            p.val = min_child.val
            p.right = self.__delete(x, p.right)
        
        # 这部分代码是用来维护AVL树的平衡性质的
        # 在递归返回的时候发挥作用
        # if only a single node, return it
        # 这个判断p为空返回的代码可以不要，因为下面的代码对空树也是有效的
        # 只是多了一些不必要的计算
        if p is None:
            return p
        # update height
        p.height = max(self.__get_height(p.left), self.__get_height(p.right)) + 1
        # re-balance
        balance_factor = self.__get_balance_factor(p)
        # 4 conditions
        # LL
        if balance_factor >= 2 and self.__get_balance_factor(p.left) >= 0:
            return self.__single_rotate_with_left(p)
        # RR
        if balance_factor <= -2  and self.__get_balance_factor(p.right) <= 0:
            return self.__single_rotate_with_right(p)
        # LR
        if balance_factor >= 2 and self.__get_balance_factor(p.left) < 0:
            return self.__double_rotate_with_left(p)
        # RL
        if balance_factor <= -2 and self.__get_balance_factor(p.left) > 0:
            return self.__double_rotate_with_right(p)
        return p
    
    
    def __pre_order(self, node):
        if node:
            print(node.val)
            self.__pre_order(node.left)
            self.__pre_order(node.right)
    
    
    def __post_order(self, node):
        if node:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print(node.val)
    
    
    def __in_order(self, node):
        if node:
            self.__in_order(node.left)
            print(node.val)
            self.__in_order(node.right)
    
    
    def __level_order(self, node):
        queue = [node,]
        while queue:
            tot = len(queue)
            level = []
            for i in range(tot):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            print(level)
            
            
    # Public Methods
    def pre_order(self):
        self.__pre_order(self.root)
    
    
    def post_order(self):
        self.__post_order(self.root)
    
    
    def in_order(self):
        self.__in_order(self.root)
    
    
    def level_order(self):
        self.__level_order(self.root)
        
            
    def insert(self, val):
        self.root = self.__insert(val, self.root)
        return self.root
    
    
    def delete(self, val):
        self.root = self.__delete(val, self.root)
        return self.root


# some tests
root = AVLTree()
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
  
for num in nums: 
    root.insert(num)

root.delete(10)  # should cause a LL rotation   
root.pre_order() # should be 1 0 -1 9 5 2 6 11


