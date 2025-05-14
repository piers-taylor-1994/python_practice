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
    def bfs(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def max_depth(self, root):
        def dfs(node, depth):
            if not node:
                return depth
            
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        
        return dfs(root, 0)
    
    def level_order(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_nodes = []

            for _ in range(len(queue)):
                node = queue.popleft()
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
        def dfs(node, depth, result):
            if not node:
                return
            if depth == len(result):
                result.append(node.value)
            dfs(node.right, depth + 1, result)
            dfs(node.left, depth + 1, result)
        result = []
        dfs(root, 0, result)
        return result
    
    def count_nodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """        
        def find_depth(node):
            depth = 0

            while node:
                depth += 1
                node = node.left

            return depth - 1
        
        def node_exists(index, depth, node):
            left = 0
            right = 2 ** depth - 1

            for _ in range(depth):
                middle = (left + right) // 2

                if index <= middle:
                    node = node.left
                    right = middle
                else:
                    node = node.right
                    left = middle + 1
            
            return node != None
        
        if not root:
            return 0
        depth = find_depth(root)
        if depth == 0:
            return 1
        
        left = 0
        right = 2 ** depth - 1

        while left <= right:
            middle = (left + right) // 2

            if node_exists(middle, depth, root):
                left = middle + 1
            else:
                right = middle - 1
        
        return left + 2 ** depth - 1
    
    def is_valid_BST(self, root):
        def dfs(node, min, max):
            if not node:
                return True
            elif not min < node.value < max:
                return False
            
            return dfs(node.left, min, node.value) and dfs(node.right, node.value, max)

        return dfs(root, -float('inf'), float('inf'))


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

#                       1
#           2                      3
#    4            5           6         7
#  8   9       10   11    12

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
node5.left = node10
node5.right = node11
node6.left = node12
print(solution.count_nodes(root))

#           7
#     5          15
#  3     6    10    21

root = TreeNode(7)
node5 = TreeNode(5)
node15 = TreeNode(15)
node3 = TreeNode(3)
node6 = TreeNode(6)
node10 = TreeNode(10)
node21 = TreeNode(21)
root.left = node5
root.right = node15
node5.left = node3
node5.right = node6
node15.left = node10
node15.right = node21
print(solution.is_valid_BST(root))