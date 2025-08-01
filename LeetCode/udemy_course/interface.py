from collections import deque

class Node:
    def __init__(self, name):
        self.Name = name
        self.Alive = True
        self.Children = []
        
class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.head = Node(kingName)
        self.people = {kingName: self.head}

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        parent = self.people[parentName]
        child = Node(childName)
        parent.Children.append(child)
        self.people[childName] = child
        
    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.people[name].Alive = False

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        results = []

        def rec(node):
            if node.Alive:
                results.append(node.Name)
            for child in node.Children:
                rec(child)

        rec(self.head)
        return results



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
print(t.getInheritanceOrder())
t.birth("shannon","scott")
t.death("clyde")
print(t.getInheritanceOrder())