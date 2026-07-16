# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        '''
        1. assign prev ptr
        2. assign curr ptr
        3. with each step move curr, prev through subsequent items in list until end
        '''

        #Initialization
        prev = None
        curr = None

        #Assign curr to head
        curr = head

        #Loop through LL until None encountered
        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev



            

