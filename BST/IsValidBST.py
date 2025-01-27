class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def isValidBST(root):
    def CheckValid(root, min_value, max_value):
        if not root:
            return True
        if root.val > min_value and root.val <max_value:
            return True
        else:
            return CheckValid(root.left,min_value,root.val) and CheckValid(root.right,root.val,max_value)
    return CheckValid(root,-float('inf'),float('inf'))

if __name__ =='__main__':
    lnode= TreeNode(1)
    rnode = TreeNode(3)
    root = TreeNode(2,lnode,rnode)
    print(isValidBST(root))

