import math
import sys
import unittest
from typing import TypeVar, Generic
from collections.abc import Callable

T = TypeVar('T')


# left child: 2i + 1
# right child: 2i + 2
# parent: (i-1) / 2
class SegmentTree(Generic[T]):
    def __init__(self, leafs: list[T], aggregator: Callable[[(T, T)], T] = sum, initial_value: T = 0):
        # n: length of leafs rounded up to a power of 2
        self.n: int = 2 ** math.ceil(math.log2(len(leafs)))
        self.aggregator = aggregator
        self.initial_value = initial_value

        self.tree: list[T] = [initial_value] * ((2 * self.n) - 1)
        for i, leaf in enumerate(leafs):
            self.tree[self.n - 1 + i] = leaf
        for i in reversed(range(self.n - 1)):
            self.tree[i] = aggregator((self.tree[2 * i + 1], self.tree[2 * i + 2]))

    def query(self, left: int, right: int):
        left = left + self.n - 1
        right = right + self.n - 1
        answer = self.initial_value

        while left <= right:
            if left % 2 == 0:
                answer = self.aggregator((answer, self.tree[left]))
                left += 1
            if right % 2 == 1:
                answer = self.aggregator((answer, self.tree[right]))
                right -= 1

            left = (left - 1) // 2
            right = (right - 1) // 2

        return answer

    def update(self, index: int, new_value: T):
        i = index + self.n - 1
        self.tree[i] = new_value

        i = (i - 1) // 2
        while i >= 0:
            self.tree[i] = self.aggregator((self.tree[2 * i + 1], self.tree[2 * i + 2]))
            i = (i - 1) // 2


class TestSegmentTreeSum(unittest.TestCase):
    def test_query(self):
        tree = SegmentTree([0, 1, 2, 3, 4], sum)
        self.assertEqual(tree.query(0, 4), 10)
        self.assertEqual(tree.query(0, 0), 0)
        self.assertEqual(tree.query(0, 1), 1)
        self.assertEqual(tree.query(1, 1), 1)
        self.assertEqual(tree.query(1, 0), 0)
        self.assertEqual(tree.query(1, 3), 6)

    def test_update_and_query(self):
        tree = SegmentTree([0, 1, 2, 3, 4], sum)

        # [-5, 1, 2, 3, 4]
        tree.update(0, -5)
        self.assertEqual(tree.query(0, 4), 5)
        self.assertEqual(tree.query(0, 0), -5)
        self.assertEqual(tree.query(0, 1), -4)

        # [-5, 1, 100, 3, 4]
        tree.update(2, 100)
        self.assertEqual(tree.query(0, 4), 103)
        self.assertEqual(tree.query(1, 3), 104)
        self.assertEqual(tree.query(2, 4), 107)


class TestSegmentTreeMin(unittest.TestCase):
    def test_query(self):
        tree = SegmentTree([3, 1, -2, 6, 4], min, sys.maxsize)
        self.assertEqual(tree.query(0, 4), -2)
        self.assertEqual(tree.query(0, 0), 3)
        self.assertEqual(tree.query(0, 1), 1)
        self.assertEqual(tree.query(1, 1), 1)
        self.assertEqual(tree.query(1, 0), sys.maxsize)
        self.assertEqual(tree.query(2, 3), -2)
        self.assertEqual(tree.query(3, 4), 4)

    def test_update_and_query(self):
        tree = SegmentTree([3, 1, -2, 6, 4], min, sys.maxsize)

        # [-1, 1, -2, 6, 4]
        tree.update(0, -1)
        self.assertEqual(tree.query(0, 4), -2)

        # [-3, 1, -2, 6, 4]
        tree.update(0, -3)
        self.assertEqual(tree.query(0, 4), -3)

        # [-3, 1, -2, 2, 4]
        tree.update(3, 2)
        self.assertEqual(tree.query(3, 4), 2)


if __name__ == '__main__':
    unittest.main()
