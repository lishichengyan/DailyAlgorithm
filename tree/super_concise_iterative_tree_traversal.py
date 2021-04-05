# For post-order traversal:
def postorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
        p = stack.pop()
        if not p[1]: continue
        stack.extend([(0, p[1]), (1, p[1].right), (1, p[1].left)]) if p[0] != 0 else res.append(p[1].val)
    return res


#For in-order traversal:
def inorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
        p = stack.pop()
        if not p[1]: continue
        stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)]) if p[0] != 0 else res.append(p[1].val)
    return res


#For pre-order traversal:
def preorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
        p = stack.pop()
        if not p[1]: continue
        stack.extend([(1, p[1].right), (1, p[1].left), (0, p[1])]) if p[0] != 0 else res.append(p[1].val)
    return res
