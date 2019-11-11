import json
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Find the first index i, from right to left, that breaks
        # a sequence of decreasing (from left to right) numbers
        i = next((i for i in range(len(nums) - 2, -1, -1) if nums[i] < nums[i + 1]), -1)
        if i >= 0:
            # Find first rightmost number that is greater than the number at i
            j = next((j for j in range(len(nums) - 1, i, -1) if nums[j] > nums[i]))
            self.swap(nums, i, j)
        self.reverse(nums, i + 1, len(nums) - 1)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, i, j):
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    def readlines():
        for line in [
            "[1, 2]",
            "[1, 3, 2]",
            "[1, 1]",
            "[1]",
            "[]",
            "[1, 2, 3]",
            "[3, 2, 1]"
        ]:
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print
                "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
