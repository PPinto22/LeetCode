# FIXME Time Limit Exceeded

import math


def solve(N, Q, candies, queries):
    def f1(i, value):
        return (-1) ** (i - 1) * value

    def f2(i, value):
        return (-1) ** (i - 1) * value * i

    def score(left, right):
        sign = (-1) ** (left - 1)
        big_area = tree2.query(left - 1, right - 1)
        subtract_area = (left - 1) * tree1.query(left - 1, right - 1)
        return sign * (big_area - subtract_area)

    tree1 = SegmentTree([f1(i + 1, sweetness) for (i, sweetness) in enumerate(candies)])
    tree2 = SegmentTree([f2(i + 1, sweetness) for (i, sweetness) in enumerate(candies)])
    answer = 0
    for query in queries:
        if query[0] == 'Q':
            answer += score(query[1], query[2])
        elif query[0] == 'U':
            tree1.update(query[1] - 1, f1(query[1], query[2]))
            tree2.update(query[1] - 1, f2(query[1], query[2]))
    return answer


# formulas:
# left child: 2i + 1
# right child: 2i + 2
# parent: (i-1) / 2
class SegmentTree:
    def __init__(self, values):
        self.n = None
        self.t = None
        self.build(values)

    def build(self, values):
        self.n = 2 ** math.ceil(math.log2(len(values)))
        self.t = [0] * (2 * self.n - 1)
        for i, leaf in enumerate(values):
            self.t[self.n - 1 + i] = leaf
        for i in reversed(range(self.n - 1)):
            self.t[i] = self.t[2 * i + 1] + self.t[2 * i + 2]

    def query(self, left, right):
        l = left + self.n - 1
        r = right + self.n - 1
        answer = 0
        while l <= r:
            if l % 2 == 0:
                answer += self.t[l]
                l += 1
            if r % 2 == 1:
                answer += self.t[r]
                r -= 1
            l = (l - 1) // 2
            r = (r - 1) // 2
        return answer

    def update(self, index, value):
        i = index + self.n - 1
        delta = value - self.t[i]
        while i >= 0:
            self.t[i] += delta
            i = (i - 1) // 2


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        N, Q = map(int, input().split())
        candies = [int(c) for c in input().split()]
        queries = []
        for j in range(Q):
            query = input().split()
            queries.append((query[0], int(query[1]), int(query[2])))
        result = solve(N, Q, candies, queries)
        print('Case #{}: {}'.format(Ti, result))
