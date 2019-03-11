# https://blog.csdn.net/Magic1an/article/details/78881665
class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x
        self.height = 0
 
class AVLTree(object):
    def __init__(self):
         self.root = None
         
    def __get_height(self, node):
        return node.height if node != None else -1
    
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
    
    def insert(self, val):
        self.root=self.__insert(val, self.root)
        return self.root
    
    def __pre(self, node):
        if node:
            print(node.val)
            self.__pre(node.left)
            self.__pre(node.right)
    
    def show(self):
        self.__pre(self.root)


root = AVLTree()
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.show()
