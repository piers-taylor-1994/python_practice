class Solution:
    def reverse_linked_list(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

solution = Solution()
print(solution.reverse_linked_list([1,2,3,4,5]))