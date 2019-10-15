import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        dummy = current = ListNode(0)
        while head:
            pair = head.next
            if pair:
                current.next = pair
                head.next = pair.next
                pair.next = head
            else:
                current.next = head
            current = head
            head = head.next
        return dummy.next


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
        for line in ["[1,2,3,4]",
                     "[]",
                     "[1]",
                     "[1,2,3,4,5]"]:
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line)

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
