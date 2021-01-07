# 9.7 
# implement an inorder traversal with O(1) space

class Tree:
    def __init__(self, parent, left, right, val):
        self.parent = parent
        self.left = left
        self.right = right
        self.val = val

    

def inorderTraversal(t):
    prev = None
    while t:
        if prev == t.parent:
            if t.left:
                t = t.left
            else:
                print(t.val)
                t = t.right or t.parent
        elif prev == t.left:
            print(t.val)
            t = t.right or t.parent
        elif prev == t.right:
            t = t.parent

