import json
from typing import List


class List_:
    def __init__(self, nums):
        self.nums = nums
        self.lower = 0
        self.upper = len(nums) - 1

    def __len__(self):
        return len(self.nums)

    def __getitem__(self, item):
        return self.nums[item]

    @classmethod
    def primaryOrSecondary(cls, l1, l2):
        l1_delta = l1.upper - l1.lower
        l2_delta = l2.upper - l2.lower
        if l1_delta > 1 and l1_delta > l2_delta:
            return l1, l2
        else:
            return l2, l1

    @classmethod
    def checkPosition(cls, l1, l2, i1, i2):
        is_even = (len(l1) + len(l2)) % 2 == 0
        value = l1[i1]
        closest = l2[i2]
        qty_below = i1 + i2 + (1 if closest < value else 0)
        qty_above = (len(l1) - i1 - 1) + (len(l2) - i2 - 1) + (1 if closest >= value else 0)

        if qty_below == qty_above:
            return "middle", None
        elif is_even and qty_above - qty_below == 1:
            candidates = [
                l1[i1 + 1] if i1 + 1 < len(l1) and l1[i1 + 1] >= value else None,
                l2[i2 + 1] if i2 + 1 < len(l2) and l2[i2 + 1] >= value else None,
                closest if closest >= value else None
            ]
            pair = min(candidate for candidate in candidates if candidate is not None)
            return "middle", pair
        elif is_even and qty_below - qty_above == 1:
            candidates = [
                l1[i1 - 1] if i1 - 1 > 0 and l1[i1 - 1] <= value else None,
                l2[l2 - 1] if l2 - 1 > 0 and l2[l2 - 1] <= value else None,
                closest if closest <= value else None
            ]
            pair = max(candidate for candidate in candidates if candidate is not None)
            return "middle", pair
        elif qty_above > qty_below:
            return "lower", None
        elif qty_below > qty_above:
            return "upper", None

    def getMiddle(self):
        index = int((self.lower + self.upper) / 2)
        return index, self.nums[index]

    def findClosest(self, target, closest='left'):
        lower = self.lower
        upper = self.upper
        i, value = self.getMiddle()
        while value != target:
            if upper - lower <= 1:
                if closest == 'left':
                    return lower, self.nums[lower]
                elif closest == 'right':
                    return upper, self.nums[upper]
                else:
                    raise AttributeError("Closest must be either 'left' or 'right'.")

            if target > value:
                lower = i
            elif target < value:
                upper = i

            i = int((lower + upper) / 2)
            value = self.nums[i]
        return i, value


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        primary, secondary = List_.primaryOrSecondary(List_(nums1), List_(nums2))

        median = None
        while median is None:
            primary, secondary = List_.primaryOrSecondary(primary, secondary)
            i1, value1 = primary.getMiddle()
            i2, value2 = secondary.findClosest(value1)
            position, pair = List_.checkPosition(primary, secondary, i1, i2)
            if position == 'middle':
                return value1 if pair is None else (value1 + pair) / 2
            elif position == 'lower':
                primary.lower = i1
                secondary.lower = i2
            elif position == 'upper':
                primary.upper = i1
                secondary.upper = i2
            else:
                raise AttributeError


def stringToIntegerList(input):
    return json.loads(input)


def main():
    lines = [
        "[1, 1]",
        "[2]"
    ].__iter__()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()