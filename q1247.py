import numpy as np


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Matrix is the count of 'x' and 'y' in s1 and s2.
        # Example, with s1 = xx and s2 = yy
        #    x  y
        # s1 2  0
        # s2 0  2
        matrix = np.array([[s.count(c) for c in ['x', 'y']] for s in [s1, s2]])
        # If the amount of Xs or Ys is odd, there is no solution
        if any(count % 2 != 0 for count in np.sum(matrix, axis=0)):
            return -1

        # Decrement the x and y count for every element that is already a match
        for x, y in zip(s1, s2):
            if x == y:
                col = ['x', 'y'].index(x)
                matrix[:, col] -= 1

        # Matrix now counts only the mismatched elements
        # There are two types of swaps to make them right:
        # Type 1 (1 swap):
        # s1: xx    yx
        #        =>
        # s2: yy    yx
        #
        # Type 2 (2 swaps):
        # s1: xy    yy    xy
        #        =>    =>
        # s2: yx    xx    xy
        type_1_pairs = sum(matrix[0] // 2)
        type_2_pairs = (sum(matrix[0]) // 2) - type_1_pairs
        return type_1_pairs + 2 * type_2_pairs


def main():
    def readlines():
        for line in ["xxyyxyxyxx","xyyxyxxxyx"]:
            yield line

    lines = readlines()
    while True:
        try:
            s1 = next(lines)
            s2 = next(lines)

            ret = Solution().minimumSwap(s1, s2)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
