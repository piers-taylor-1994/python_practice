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