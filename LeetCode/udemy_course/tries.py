class TrieNode:
    def __init__(self):
        self.Is_end = False
        self.Children = [None] * 26
        
class Trie(object):
    def __init__(self):
        self.Root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.Root

        for letter in word:
            alphabet_idx = ord(letter) - ord("a")

            if not current.Children[alphabet_idx]:
                current.Children[alphabet_idx] = TrieNode()

            current = current.Children[alphabet_idx]
        
        current.Is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.Root

        for letter in word:
            alphabet_idx = ord(letter) - ord("a")

            if not current.Children[alphabet_idx]:
                return False

            current = current.Children[alphabet_idx]
        
        return current.Is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        current = self.Root

        for letter in prefix:
            alphabet_idx = ord(letter) - ord("a")

            if not current.Children[alphabet_idx]:
                return False

            current = current.Children[alphabet_idx]
        
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = print(obj.search("appls"))
param_3 = print(obj.startsWith("app"))