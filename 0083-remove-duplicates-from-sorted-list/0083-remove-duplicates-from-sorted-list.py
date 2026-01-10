# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head

        while cursor and cursor.next:
            if cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            else:
                if cursor.val != cursor.next.val:
                    cursor = cursor.next
        return head