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
    
    def breath_first_search(self):
        current_node = self.root
        list = []
        queue = []
        queue.append(current_node)

        while queue:
            current_node = queue.pop(0)
            print(current_node.value)
            list.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return list
    
    def traverse_in_order(self, node, list):
        if node.left:
            self.traverse_in_order(node.left, list)
        list.append(node.value)
        if node.right:
            self.traverse_in_order(node.right, list)
        return list
    
    def DFS_in_order(self):
        return self.traverse_in_order(self.root, [])
    
    def traverse_pre_order(self, node, list):
        list.append(node.value)
        if node.left:
            self.traverse_pre_order(node.left, list)
        if node.right:
            self.traverse_pre_order(node.right, list)
        return list
    
    def DFS_pre_order(self):
        return self.traverse_pre_order(self.root, [])
    
    def traverse_post_order(self, node, list):
        if node.left:
            self.traverse_post_order(node.left, list)
        if node.right:
            self.traverse_post_order(node.right, list)
        list.append(node.value)
        return list

    def DFS_post_order(self):
        return self.traverse_post_order(self.root, [])
    
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

    def max_depth(self, node, count = 0):
        if not node:
            return count
        count += 1

        return max(self.max_depth(node.left, count), self.max_depth(node.right, count))

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

# print(bst_tree.breath_first_search())
# print(bst_tree.DFS_in_order())
# print(bst_tree.DFS_pre_order())
# print(bst_tree.DFS_post_order())

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

print(root.max_depth(root))