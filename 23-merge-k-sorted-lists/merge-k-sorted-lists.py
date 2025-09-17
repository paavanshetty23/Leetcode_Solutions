# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergetwo(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            if list1.val <= list2.val:
                curr = list1
                curr.next = mergetwo(list1.next, list2)
            else:
                curr = list2
                curr.next = mergetwo(list1, list2.next)

            return curr

        new = lists[0]
        for i in range(1, len(lists)):
            new = mergetwo(new, lists[i])

        return new
