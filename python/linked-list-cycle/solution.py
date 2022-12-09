from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def linked_list_has_cycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow_iterator = head
        fast_iterator = head

        while fast_iterator.next and fast_iterator.next.next:
            slow_iterator = slow_iterator.next
            fast_iterator = fast_iterator.next.next

            if slow_iterator == fast_iterator:
                return True

        return False
