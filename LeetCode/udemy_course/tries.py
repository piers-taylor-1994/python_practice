class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root

        for letter in word:
            alphabet_idx = ord(letter) - ord("a")

            if not current.children[alphabet_idx]:
                current.children[alphabet_idx] = TrieNode()

            current = current.children[alphabet_idx]
        
        current.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word_length = len(word)

        def dfs(node, letter_num):
            if not node:
                return False
            elif letter_num == word_length - 1:
                return node.end
            
            letter_num += 1
            return dfs(node.children[ord(word[letter_num]) - ord("a")], letter_num)

        return dfs(self.root, -1)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        word_length = len(prefix)

        def dfs(node, letter_num):
            if not node:
                return False
            elif letter_num == word_length - 1:
                return True
            
            letter_num += 1
            return dfs(node.children[ord(prefix[letter_num]) - ord("a")], letter_num)

        return dfs(self.root, -1)

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = print(obj.search("appls"))
param_3 = print(obj.startsWith("app"))