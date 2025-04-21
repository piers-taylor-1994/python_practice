class Node:
    def __init__(self, value):
        self.value = value  # Store the value of the node
        self.next = None    # Point to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list (initially None)

    def append(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

class Solution:
    def reverse_linked_list(self, head):
        prev = None
        current = head
        while current:
            next = current.next #Record the next node before we change the data around
            current.next = prev #Reverse the pointers (as we're reversing the list) (before this, it's still pointing forward 1=>2=>3, we want it the reverse 3=>2=>1=>null etc)
            prev = current #Record the current state of the linked array (move the previous prev forward)
            current = next #Move to the next node
        return prev
    
    def reverse_partial_linked_list(self, head, left, right):
        position = 1
        current = head
        start = head

        while position < left:
            start = current
            current = current.next
            position += 1
        
        tail = current
        new_list = None

        while position >= left and position <= right:
            next = current.next
            current.next = new_list
            new_list = current
            current = next
            position += 1

        start.next = new_list
        tail.next = current

        if left > 1:
            return head
        return new_list
    
solution = Solution()
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.display()
linked_list.reverse()
linked_list.display()