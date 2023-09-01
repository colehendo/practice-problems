from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class ListNode:
    val: int
    next = None


class Solution:
    def find_list_length_and_last_node(self, head: ListNode) -> Tuple[ListNode, int]:
        current_node = head
        list_length = 1
        while current_node.next:
            current_node = current_node.next
            list_length += 1

        return current_node, list_length

    @staticmethod
    def rotate_list(node: ListNode, list_length: int, num_rotations: int):
        for i in range(list_length - (num_rotations % list_length) - 1):
            node = node.next

    def reorder_list(
        self, head: ListNode, last_node: ListNode, list_length: int, num_rotations: int
    ):
        last_node.next = head
        front_node = head

        self.rotate_list(front_node, list_length, num_rotations)

        final_node = front_node.next
        front_node.next = None

        return final_node

    def handle_list_rotation(
        self, head: Optional[ListNode], num_rotations: int
    ) -> Optional[ListNode]:
        if num_rotations == 0 or not head:
            return head

        last_node, list_length = self.find_list_length_and_last_node(head)

        if num_rotations % list_length == 0:
            return head

        new_head = self.reorder_list(head, last_node, list_length, num_rotations)

        return final_node
