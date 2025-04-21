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
        current_position = 1
        current_node = head
        start = head

        #While current_position is before the soon-to-be reversed part
        while current_position < left:
            start = current_node #start will always eventually be the node before the reversed part (left - 1)
            current_node = current_node.next
            current_position += 1
        
        #Since the previous while loop has finished, that means we're in the reversed part therefore tail is the current node
        tail = current_node
        new_reversed_list = None #Used to be called prev

        #Same as in the previous solution, apart from iterating current_position
        while current_position >= left and current_position <= right:
            next = current_node.next
            current_node.next = new_reversed_list
            new_reversed_list = current_node
            current_node = next
            current_position += 1

        #While drawing out the before and after, highlighting the node before (start) and the tail of the reversed list part (tail) makes it obvious which points at what
        start.next = new_reversed_list #The start (before reversed part) equals to the new reversed list
        tail.next = current_node #The end of the reversed list now points at the node after we need to reverse

        #This is to make sure that they don't want the reversing to start at the beginning. If they do, head won't be valid anymore, as it'll be now the tail.
        #Therefore we want to return reversed_list, as this is the head of the new reversed_list (the last value of new list is the new head thefore == new_versed_list)
        if left > 1:
            return head
        return new_reversed_list
    
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