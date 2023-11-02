import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self._combined_list_node: Optional[ListNode] = None
        self._combined_list_node_head: Optional[ListNode] = None

    @property
    def combined_list_node(self):
        return self._combined_list_node

    @combined_list_node.setter
    def combined_list_node(self, node: ListNode):
        self._combined_list_node = node

    @property
    def combined_list_node_head(self):
        return self._combined_list_node_head

    @combined_list_node_head.setter
    def combined_list_node_head(self, node: ListNode):
        self._combined_list_node_head = node

    def add_node(self, node_value: int, last_node: Optional[ListNode] = None):
        if last_node is None:
            last_node = self.combined_list_node

        new_node = ListNode(val=node_value)
        last_node.next = new_node
        self.combined_list_node = new_node

    def bubble_up_value(self, node: ListNode, additional_value: Optional[int] = 0):
        if node is None:
            return

        combined_value = node.val + additional_value

        if combined_value > 9:
            remainder = combined_value % 10
            next_value = math.floor(combined_value / 10)

            node.val = remainder

            if node.next is None:
                self.add_node(next_value, node)
                return self.bubble_up_value(self.combined_list_node)
            else:
                return self.bubble_up_value(node.next, next_value)
        else:
            node.val = combined_value
            if node.next is not None:
                self.bubble_up_value(node.next)

    def handle_combined_value(self, value_to_add: int):
        if not self.combined_list_node:
            self.combined_list_node = ListNode(val=value_to_add)
            self.combined_list_node_head = self.combined_list_node
            self.handle_combined_value = self.add_node
        else:
            self.add_node(self.combined_value)

    def add_two_numbers(
        self, first_list: Optional[ListNode], second_list: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Deal with initial edge cases
        if not first_list:
            return second_list
        if not second_list:
            return first_list
        if not first_list and not second_list:
            return self.combined_list_node

        # Combine the two lists
        while first_list is not None and second_list is not None:
            combined_value = first_list.val + second_list.val
            self.handle_combined_value(combined_value)

            first_list = first_list.next
            second_list = second_list.next

        # Deal with larger lists
        while first_list is not None:
            self.add_node(first_list.val)
            first_list = first_list.next
        while second_list is not None:
            self.add_node(second_list.val)
            second_list = second_list.next

        # Ensure each node has a value under 10,
        # bubble the remainder up to higher nodes
        self.bubble_up_value(self.combined_list_node_head)

        return self.combined_list_node_head
