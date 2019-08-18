import json

from q0002 import ListNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = self.get_list_size(head)
        remove_node_idx = size - n

        dummy = ListNode(0)
        dummy.next = head

        closest_node = dummy
        for _ in range(remove_node_idx):
            closest_node = closest_node.next
        closest_node.next = closest_node.next.next

        return dummy.next

    def get_list_size(self, head):
        size = 0
        while head is not None:
            size += 1
            head = head.next
        return size


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
    def readlines():
        for line in ["[1,2,3,4,5]", "2",
                     "[1,2]", "2"]:
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            n = int(line);

            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
