# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or not head.next:
            return head

        newHead = self.reverseList(head.next)

        head.next.next =head

        head.next = None

        return newHead
        
        # if head is None:
        #     return None
        # prev = None
        # current = head
        # while current is not None:
        #     temp_node = current.next  
        #     current.next = prev          
        #     prev = current            
        #     current = temp_node
        # return prev
