# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle edge case where the head itself needs to be removed
        while head is not None and head.val == val:
            head = head.next
        
        # Use a temporary pointer to iterate through the list
        temp = head
        while temp is not None and temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
