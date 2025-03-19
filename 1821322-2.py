class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def compute_depth(root):
    if root is None:
        return 0
    left_depth = compute_depth(root.left)
    right_depth = compute_depth(root.right)
    return 1 + max(left_depth, right_depth)


# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Counting nodes
print("Number of nodes:", count_nodes(root))

# Computing depth
print("Depth of the tree:", compute_depth(root))
