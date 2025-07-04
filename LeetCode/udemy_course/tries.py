class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.alphabet = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root

        for letter in word:
            idx = ord(letter) - ord("a")

            if idx not in current.children:
                current.children[idx] = TrieNode()

            current = current.children[idx]
        
        current.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root

        for letter in word:
            idx = ord(letter) - ord("a")

            if idx not in current.children:
                return False

            current = current.children[idx]
        
        return current.end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root

        for letter in prefix:
            idx = ord(letter) - ord("a")

            if idx not in current.children:
                return False

            current = current.children[idx]
        
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = print(obj.search("appls"))
param_3 = print(obj.startsWith("app"))