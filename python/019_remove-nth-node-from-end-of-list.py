'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        is_at_tail = False

        if head.next == None:
            return None

        window_buffer_list : List[ListNode] = []
        current_node = head
        number_of_elements = 0
        while not is_at_tail:

            window_buffer_list.append(current_node)
            number_of_elements += 1

            # keep track of one more than the target so that we can tie it to the next one
            buffer_window_max_size = n+1
            if len(window_buffer_list) > buffer_window_max_size:
                window_buffer_list.pop(0)

            if current_node.next == None:
                # we are at the tail
                is_at_tail = True
            else:
                current_node = current_node.next


        index_to_ele_to_remove = len(window_buffer_list) - n

        if index_to_ele_to_remove == 0:
            # This means we didn't even have enough events to fill our buffer window
            # and the user requested the HEAD to be removed
            return window_buffer_list[1]
        else:
            window_buffer_list[index_to_ele_to_remove - 1].next = window_buffer_list[index_to_ele_to_remove].next

        return head
