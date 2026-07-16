# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        1. cycle through linked list
        2. check if item present in unique ptr set 
        3. store seen objects in set if not present
        4. return true if obj present in unique ptr set
        '''

        uniquePtrSet = set()

        curPtr = head

        while(curPtr):
            print (str(curPtr.val))
            print (str(curPtr.next))

            if(curPtr in uniquePtrSet):
                return True
            else:
                uniquePtrSet.add(curPtr)
                curPtr = curPtr.next

        return False

        