'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        max_no_of_nodes = 100

        head = ListNode(-1)
        current_node = head
        l1_temp = l1
        l2_temp = l2
        carry = 0

        for i in range(max_no_of_nodes):
            sum = carry
            carry = 0

            if (l1_temp == None) and (l2_temp == None):
                break
            if l1_temp != None:
                sum += l1_temp.val
                l1_temp = l1_temp.next

            if l2_temp != None:
                sum += l2_temp.val
                l2_temp = l2_temp.next

            carry = sum // 10
            sum = sum % 10
            new_node = ListNode(sum)
            current_node.next = new_node
            current_node = current_node.next

        if sum != 0:
            new_node = ListNode(sum)
            current_node.next = new_node

        return head.next


from list_nodes_helper import *

node_list = genNodesList([[9,9,9,9,9,9,9], [9,9,9,9]])

int_list = nodesToIntList((Solution()).addTwoNumbers(node_list[0], node_list[1]))
print(int_list)
