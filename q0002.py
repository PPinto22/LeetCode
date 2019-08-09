# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, _carry: int = 0) -> ListNode:
        if l1 is None and l2 is None:
            if _carry > 0:
                return ListNode(_carry)
            else:
                return None
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)

        node_sum = l1.val + l2.val + _carry
        node_val = node_sum % 10
        node_carry = node_sum // 10
        node = ListNode(node_val)
        node.next = self.addTwoNumbers(l1.next, l2.next, _carry=node_carry)
        return node


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
    lines = [
        "[0]",
        "[7,3]"
    ].__iter__()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
