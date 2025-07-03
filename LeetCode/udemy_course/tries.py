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
        current = self.root

        for letter in word:
            alphabet_idx = ord(letter) - ord("a")

            if not current.children[alphabet_idx]:
                return False

            current = current.children[alphabet_idx]
        
        return current.end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        current = self.root

        for letter in prefix:
            alphabet_idx = ord(letter) - ord("a")

            if not current.children[alphabet_idx]:
                return False

            current = current.children[alphabet_idx]
        
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = print(obj.search("appls"))
param_3 = print(obj.startsWith("app"))