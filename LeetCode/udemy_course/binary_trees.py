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
from collections import deque
import math
from os import curdir


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
        result = []
        queue = [current_node]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
        
    
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
    def DFS_pre_order_iterative(self):
        current_node = self.root
        result = []
        stack = [current_node]

        while stack:
            current_node = stack.pop()
            result.append(current_node.value)

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
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
    def DFS_in_order_iterative(self):
        current_node = self.root
        result = []
        stack = []

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()
            result.append(current_node.value)

            current_node = current_node.right
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
    def DFS_post_order_iterative(self):
        current_node = self.root
        result = []
        stack1 = [current_node]
        stack2 = []

        while stack1:
            current_node = stack1.pop()
            stack2.append(current_node)

            if current_node.left:
                stack1.append(current_node.left)
            if current_node.right:
                stack1.append(current_node.right)
        
        while stack2:
            result.append(stack2.pop().value)
        
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

class Solution:
    def max_depth(self, root):
        def helper(node, depth):
            if not node:
                return depth
            depth += 1

            return max(helper(node.left, depth), helper(node.right, depth))
        return helper(root, 0)
    
    def level_order(self, root):
        if not root:
            return []
        node = root
        result = []
        # queue = deque([node]) //More efficient O(n) => O(1) time
        queue = [node]
        
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                #node = queue.popleft() //More efficient O(n) => O(1) time as pop(0) shifts values
                node = queue.pop(0)
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
    
    def right_side_view_BFS(self, root):
        if not root:
            return []
        node = root
        result = []
        queue = deque([node])

        while queue:
            right_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                right_node = node.value

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(right_node)
        return result
    
    def right_side_view_DFS(self, root):
        def helper(node, result, depth):
            if not node:
                return
            if depth == len(result):
                result.append(node.value)
            
            helper(node.right, result, depth + 1)
            helper(node.left, result, depth + 1)
        result = []
        helper(root, result, 0)
        return result
    
    def count_nodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def find_height(node, height):
            if not node:
                return
            
            height += 1
            if not node.left and not node.right:
                return height
            return find_height(node.left, height)

        def node_exists(index, height, node):
            left = 0
            right = (2 ** height) - 1
            count = 0
            
            while count < height:
                middle_of_node = math.ceil((left + right) / 2)
                if index >= middle_of_node:
                    node = node.right
                    left = middle_of_node
                else:
                    node = node.left
                    right = middle_of_node - 1
                count += 1
            
            return node != None
        
        if not root:
            return 0
        height = find_height(root, 0)

        if height == 1:
            return 1

        bottom_max = (2 ** height) - 1

        left = 0
        right = bottom_max

        while left < right:
            index_to_find = math.ceil((left + right) / 2)
            if node_exists(index_to_find, bottom_max, root):
                left = index_to_find
            else:
                right = index_to_find - 1

        return bottom_max + left + 1

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

# print(bst_tree.BFS())
print(bst_tree.DFS_pre_order())
print(bst_tree.DFS_pre_order_iterative())
print(bst_tree.DFS_in_order())
print(bst_tree.DFS_in_order_iterative())
print(bst_tree.DFS_post_order())
print(bst_tree.DFS_post_order_iterative())

#         1
#     2         3
# 4      5              6
#     7
#  8
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.right = node7
node7.left = node8

print(solution.max_depth(root))
print(solution.level_order(root))
print(solution.level_order(None))

print(solution.right_side_view_BFS(root))
print(solution.right_side_view_BFS(root))

#          1
#      2       3
# 4       5  6

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
print(solution.count_nodes(root))