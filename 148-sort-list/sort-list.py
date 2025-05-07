# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findmid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.findmid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.merge(left, right)
