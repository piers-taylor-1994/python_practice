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
# BFS

from os import curdir


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

class Solution:
    pass

solution = Solution()

#       9
#   4       20
#1    6   15   170  

tree = BST()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree.breath_first_search())
print(tree.DFS_in_order())
print(tree.DFS_pre_order())
print(tree.DFS_post_order())