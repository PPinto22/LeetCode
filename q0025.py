# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = current = ListNode(0)
        while head:
            head, is_reversed, group_tail, next_group = self._reverseKGroupRecursive(head, k)
            current.next = head
            head = next_group
            current = group_tail
        return dummy.next

    def _reverseKGroupRecursive(self, head, k, previous=None, i=0):
        if not head:
            return head, False, previous, None
        if k == 1:
            return head, False, head, head.next
        if i == k - 1:
            next_group = head.next
            head.next = previous
            return head, True, None, next_group

        new_head, is_reversed, group_tail, next_group = self._reverseKGroupRecursive(head.next, k, head, i + 1)
        if is_reversed:
            if i == 0:
                head.next = next_group
                group_tail = head
            else:
                head.next = previous
            return new_head, is_reversed, group_tail, next_group
        else:
            return head, is_reversed, group_tail, next_group


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in ["[1,2,3,4,5]", "2",
                     "[]", "1",
                     "[1,2,3,4,5]", "1",
                     "[1,2,3,4,5,6,7]", "3"]:
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            k = int(line);

            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
