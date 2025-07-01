from collections import deque


class Node():
    def __init__(self, name, parent):
        self.Name = name
        self.Parent = parent
        self.Children = []

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
                children = current.Children
                parent = current.Parent

                if not parent or not parent:
                    if not parent:
                        new_king = children[0]
                        self.head = new_king
                        new_king.Parent = None
                    if not children:
                        parent.Children.remove(current)
                else:
                    index = parent.Children.index(current)

                    for child in children:
                        parent.Children.insert(index, child)
                        index += 1
                    parent.Children.remove(current)

                    for child in children:
                        child.Parent = parent
                
                current.Parent = None
                current.Children = None
                break
            queue += current.Children

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        results = []

        def dfs(node):
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