from wsgiref import headers


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
    
    def flatten_doubly_linked_list(self, head):
        #if linked list is null, return null
        if not head:
            return None
        
        currentNode = head

        #loop through all the nodes
        while currentNode:
            #if the current node has a child
            if currentNode.child:
                #Initialise variables before we change current node's properties
                child = currentNode.child
                next = currentNode.next

                #Set the before node (current node) and child head's node (child) next/prev
                currentNode.next = child
                child.prev = currentNode

                #If there is a node after the current node, we need to worry about setting it's prev and the tail's next
                if next:
                    while child.next:
                        child = child.next
                    tail = child #could just be child but calling it tail is more readable
                    tail.next = next
                    next.prev = tail
                currentNode.child = None #Set the current node's child to null after we've dealt with it
            currentNode = currentNode.next #Move onto next node
        return head
    
    def has_cycle(self, head):
        if not head:
            return False
        current = head
        seen_nodes = set()

        while current not in seen_nodes:
            if not current.next:
                return False
            seen_nodes.add(current)
            current = current.next
        return True
    
    def has_cycle_floyd(self, head):
        if not head or not head.next:
            return False
        tort = head
        hare = head

        while True:
            tort = tort.next
            hare = hare.next

            if not hare or not hare.next:
                return False
            hare = hare.next

            if tort == hare:
                return True
    
    def has_cycle_2(self, head):
        if not head:
            return None
        current = head
        seen_nodes = set()

        while current not in seen_nodes:
            if not current.next:
                return None
            seen_nodes.add(current)
            current = current.next
        return current