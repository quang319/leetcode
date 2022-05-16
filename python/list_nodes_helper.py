from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def genNodesList(valueList: List[List[int]]) -> List[ListNode]:
    nodes_list = []

    for int_list in valueList:
        head_node = ListNode(-1)
        current_node = head_node
        for index in range(len(int_list)):
            temp_node = ListNode(int_list[index])

            current_node.next = temp_node
            current_node = current_node.next

        if head_node.next != None:
            nodes_list.append(head_node.next)
    return nodes_list

def nodesListToIntList(nodesList: List[ListNode]) -> List[List[int]]:
    int_list = []
    for node in nodesList:
        current_node: ListNode = node
        current_list = []
        current_list.append(current_node.val)

        while current_node.next != None:
            current_node = current_node.next
            current_list.append(current_node.val)

        if len(current_list) > 0:
            int_list.append(current_list)

    return int_list

def nodesToIntList(node: ListNode) -> List[int]:
    if node == None:
        return []

    current_node: ListNode = node
    current_list = []
    current_list.append(current_node.val)

    while current_node.next != None:
        current_node = current_node.next
        current_list.append(current_node.val)

    return current_list