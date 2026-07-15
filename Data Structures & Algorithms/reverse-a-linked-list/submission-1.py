# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Temporarily save the next node so we don't lose it
            curr.next = prev  # Reverse the arrow! (Point backward)
            prev = curr       # Move prev forward
            curr = nxt        # Move curr forward
            
        return prev  # prev will end up pointing to the new head of the reversed list


