# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        


        '''
        0. initizlie a dummy node
        1. create curr pointer to the dummy node
        2. if list1 & list2 exists
            a. compare first elem of both
            b. get the smaller elem.val and assign it to the curr pointer
            c. update the start node of the list from which the value is removed
            d. increment the curr to the .next value of elem.val
        3. else
            a. append the remaining list to the tail end
        4. return dummy start pointer
        '''



        dummyObj = ListNode(val=-1)
        curr = dummyObj
        persistStartPtr = dummyObj

        while (list1 and list2):
            if(list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # #If either remaining, append
        if (list1):
            curr.next = list1
        if (list2):
            curr.next = list2

        return dummyObj.next












            