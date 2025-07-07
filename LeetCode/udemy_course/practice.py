from collections import deque
import random
 
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for letter in word:
            letter_idx = ord(letter) - ord("a")

            if not current_node.children[letter_idx]:
                current_node.children[letter_idx] = TrieNode()
            
            current_node = current_node.children[letter_idx]
        
        current_node.end = True
    
    def search_word(self, word):
        current_node = self.root

        for letter in word:
            letter_idx = ord(letter) - ord("a")

            if not current_node.children[letter_idx]:
                return False
            
            current_node = current_node.children[letter_idx]
        
        return current_node.end
    
    def search_prefix(self, prefix):
        current_node = self.root

        for letter in prefix:
            letter_idx = ord(letter) - ord("a")

            if not current_node.children[letter_idx]:
                return False
            
            current_node = current_node.children[letter_idx]
        
        return True

class Solution:
    """
    1. Arrays
    2. Strings
    3. Sorts/searches
    4. Linked lists
    5. Binary trees
    6. Tries
    7. Matrices
    8. Stack/queues
    9. Graphs
    10. Heaps
    11. DP
    12. Backtracking

    """
    def two_sum(self, nums, target):
        recorded_nums = {}
        def rec(i):
            if (target - nums[i]) in recorded_nums:
                return [recorded_nums[target - nums[i]], i]
            
            recorded_nums[nums[i]] = i
            return rec(i + 1)
        return rec(0)
    
    def is_palindrome(self, s):
        word = "".join([letter for letter in s if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]).lower()
        
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def linked_list_has_cycle(self, head):
        if not head or not head.next:
            return False
        
        visited_nodes = set()
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next

    def binary_tree_bfs(self, root):
        if not root:
            return []
        
        queue = deque([root])
        tree = []

        while queue:
            current_node = queue.popleft()
            tree.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return tree
    
    def binary_tree_dfs(self, root, dfs_type):
        tree = []

        def dfs(node):
            if not node:
                return
            
            if dfs_type == "preorder":
                tree.append(node.val)
                dfs(node.left)
                dfs(node.right)
            elif dfs_type == "inorder":
                dfs(node.left)
                tree.append(node.val)
                dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)
                tree.append(node.val)
            
        dfs(root)
        return tree 

# print(random.choice(["container-with-most-water", "trapping-rainwater"]))
# print(random.choice(["typed-out-strings", "longest-substring-without-repeating", "is_almost_palindrome"]))
# print(random.choice(["quick_sort", "binary_search"]))
# print(random.choice(["reverse_partial_linked_list", "flatten_double_linked_list"]))
# print(random.choice(["max-depth", "level-order", "right-side-view", "count-nodes", "is_valid_bst"]))

solution = Solution()

print(solution.two_sum([3,2,4], 6))

print(solution.is_palindrome("A man, a plan, a canal: Panama"))

head = ListNode(3)
node_1 = ListNode(2)
node_2 = ListNode(0)
node_3 = ListNode(-4)
head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_1
print(solution.linked_list_has_cycle(head))

root = TreeNode(1)
tree_node_2 = TreeNode(2)
tree_node_3 = TreeNode(3)
tree_node_4 = TreeNode(4)
tree_node_5 = TreeNode(5)
tree_node_6 = TreeNode(6)
root.left = tree_node_2
root.right = tree_node_3
tree_node_2.left = tree_node_4
tree_node_2.right = tree_node_5
tree_node_3.left = tree_node_6
print(solution.binary_tree_bfs(root))
print("/// dfs ///")
print(solution.binary_tree_dfs(root, "preorder"))
print(solution.binary_tree_dfs(root, "inorder"))
print(solution.binary_tree_dfs(root, "postorder"))

trie = Trie()
trie.insert("appls")
print(trie.search_word("apple"))
print(trie.search_prefix("app"))