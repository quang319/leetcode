'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
'''
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (lists == None) or (len(lists) == 0):
            return None
        return self.merge_lists(lists, 0, len(lists)-1 )

    def merge_lists(self, lists: List[Optional[ListNode]], start, end):
        # base condition
        if start == end:
            return lists[start]

        half = start + ((end - start) // 2)

        left = self.merge_lists(lists, start, half)
        right = self.merge_lists(lists, half+1, end)

        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode):
        head = ListNode(-1)
        current_node = head

        # loop over and sort until left or right is empty
        while (left != None) and (right != None):
            if left.val < right.val:
                current_node.next = left
                left = left.next
            else:
                current_node.next = right
                right = right.next

            current_node = current_node.next

        # either left or right should be empty at this point
        while left != None:
            current_node.next = left
            left = left.next
            current_node = current_node.next

        while right != None:
            current_node.next = right
            right = right.next
            current_node = current_node.next

        return head.next


from list_nodes_helper import *

# node_list = genNodesList([[1,4,5],[1,3,4],[2,6]])
node_list = genNodesList([[],[-1,5,11],[],[6,10]])

int_list = nodesToIntList((Solution()).mergeKLists(node_list))
print(int_list)
