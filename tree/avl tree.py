class TreeNode():
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x
        self.height = 0
 
 class AVLTree():
     def __init__(self):
         self.root = None
         
    def get_height(self, node):
        return height if node != None else -1
    
    def single_rotate_with_left(self, k2):
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
        k2.height = max(self.get_height(k2.left), self.get_height(k2.right)) + 1
        k1.height = max(self.get_height(k1.left), k2.height) + 1 
        return k1
    
    def single_rotate_with_right(self, k2):
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
        k2.height = max(self.get_height(k2.left), self.get_height(k2.right)) + 1
        k1.height = max(self.get_height(k1.right), k2.height) + 1 
        return k1
    
    def double_rotate_with_left(self, k3):
        """
             k3             k2
            /  \           /  \
            k1  D   ===>   k1  K3  
           /  \           / \  / \
          A   k2         A  B  C  D
              / \
              B  C       
        """
        k3.left = self.single_rotate_with_right(k3.left)
        return self.single_rotate_with_left(k3)
    
        
    def double_rotate_with_right(self, k3):
        """
             k3             k2
            /  \           /  \
            A  K1   ===>   k1  K3  
              /  \        / \  / \
             k2   D       A  B  C  D
             / \
             B  C       
        """
        k3.right = self.single_rotate_with_left(k3.right)
        return self.single_rotate_with_right(k3)
    
    def insert(self, x, p):
        if p == None:
            p = TreeNode(x)
        elif x < p.val:
            p.left = self.insert(x, p.left)
            if self.get_height(p.left) - self.get_height(p.right) == 2:
                if x < p.left.val:
                    p = self.single_rotate_with_left(p)
                else:
                    p = self.double_rotate_with_left(p)
        elif x > p.val:
            p.right = self.insert(x, p.right)
            if self.get_height(p.right) - self.get_height(p.left) == 2:
                if x > p.right.val:
                    p = self.single_rotate_with_right(p)
                else:
                    p = self.double_rotate_with_right(p)
        else:
            pass
        p.height = max(self.get_height(p.left), self.get_height(p.right)) + 1 
        return p
    
    def pre(self):
        if self.root:
            print(self.root.val)
            self.pre(self.root.left)
            self.pre(self.root.right)

