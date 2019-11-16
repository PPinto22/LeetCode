# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = current = ListNode(0)
        # Remove empty lists
        lists = [l for l in lists if l is not None]
        while any(lists):
            # Find node with the smallest value
            index, node = min(enumerate(lists), key=lambda x: x[1].val)
            current.next = node
            current = current.next
            if node.next:
                lists[index] = node.next
            else:
                del lists[index]

        return dummy.next