#If you know a solution is not far from the root of the tree:
# BFS

# If the tree is very deep and solutions are rare: 
# BFS (DFS will take too long)

# If the tree is very wide:
# DFS (BFS will use too much memory)

# If solutions are frequent but located deep in the tree:
# DFS

# Determining whether a path exists between two nodes:
# DFS

# Finding the shortest path:
# BF

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def BFS(self):
        if not self.root:
            return []
        current_node = self.root
        list = []
        queue = [current_node]

        while queue:
            current_node = queue.pop(0)
            list.append(current_node.value)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return list
        
    
    def DFS_pre_order(self):
        """Root -> left -> right"""
        def helper(node, result):
            if not node:
                return
            
            result.append(node.value)
            if node.left:
                helper(node.left, result)
            if node.right:
                helper(node.right, result)
        result = []
        helper(self.root, result)
        return result
    def DFS_in_order(self):
        """left -> root -> right"""
        def helper(node, result):
            if not node:
                return
            
            if node.left:
                helper(node.left, result)
            result.append(node.value)
            if node.right:
                helper(node.right, result)
        result = []
        helper(self.root, result)
        return result
    def DFS_post_order(self):
        """left -> right -> root"""
        def helper(node, result):
            if not node:
                return

            if node.left:
                helper(node.left, result)
            if node.right:
                helper(node.right, result)
            result.append(node.value)
        result = []
        helper(self.root, result)
        return result
    def DFS_all(self, version):
        def helper(node, result, version):
            if not node:
                return
            
            if version == "preorder":
                result.append(node.value)
            if node.left:
                helper(node.left, result, version)
            if version == "inorder":
                result.append(node.value)
            if node.right:
                helper(node.right, result, version)
            if version == "postorder":
                result.append(node.value)
        result = []
        helper(self.root, result, version)
        return result

    
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initializes a binary tree node.

        :param val: The value of the node
        :param left: Reference to the left child node
        :param right: Reference to the right child node
        """
        self.value = value
        self.left = left
        self.right = right

    def max_depth(self, node, depth = 0):
        if not node:
            return depth
        depth += 1

        return max(self.max_depth(node.left, depth), self.max_depth(node.right, depth))

class Solution:
    pass

solution = Solution()

bst_tree = BST()

#       9
#   4       20
#1    6   15   170  

bst_tree.insert(9)
bst_tree.insert(4)
bst_tree.insert(6)
bst_tree.insert(20)
bst_tree.insert(170)
bst_tree.insert(15)
bst_tree.insert(1)

print(bst_tree.BFS())
print(bst_tree.DFS_all("preorder"))
print(bst_tree.DFS_all("inorder"))
print(bst_tree.DFS_all("postorder"))
print(bst_tree.DFS_pre_order())
print(bst_tree.DFS_in_order())
print(bst_tree.DFS_post_order())

#        1
#    2       3
# 4            5
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
root.left = node2
node2.left = node4
root.right = node3
node3.right = node5

# print(root.max_depth(root))