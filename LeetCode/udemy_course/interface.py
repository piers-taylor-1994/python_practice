from collections import deque


class Node():
    def __init__(self, name, parent):
        self.Name = name
        self.Children = []
        self.Alive = True

    def add_children(self, child):
        self.Children.append(child)
        
class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.head = Node(kingName, None)

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        current = self.head
        queue = deque([current])

        while queue:
            current = queue.popleft()
            if current.Name == parentName:
                current.Children.append(Node(childName, current))
                break
            queue += current.Children

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        current = self.head
        queue = deque([current])

        while queue:
            current = queue.popleft()
            if current.Name == name:
                current.Alive = False
                break
            queue += current.Children

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        results = []

        def dfs(node):
            if node.Alive:
                results.append(node.Name)
            for child in node.Children:
                dfs(child)

        dfs(self.head)
        print(results)


# Your ThroneInheritance object will be instantiated and called as such:
# t = ThroneInheritance("king")
# t.birth("king", "andy")
# t.birth("king", "bob")
# t.birth("king", "catherine")
# t.birth("andy", "matthew")
# t.birth("bob", "alex")
# t.birth("bob", "asha")
# t.getInheritanceOrder()
# t.death("bob")
# t.getInheritanceOrder()

t = ThroneInheritance("king")
t.birth("king", "clyde")
t.death("king")
t.birth("clyde","shannon")
t.getInheritanceOrder()
t.birth("shannon","scott")
t.death("clyde")
t.getInheritanceOrder()