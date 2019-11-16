from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict[num] + 1 if num in nums_dict else 1

        for i in range(len(nums) - 2):
            n1 = nums[i]
            if i > 0 and nums[i - 1] == n1:
                continue
            for j in range(i + 1, len(nums) - 1):
                n2 = nums[j]
                if (n1 == n2 and nums_dict[n2] < 2) or (j > i + 1 and nums[j - 1] == n2):
                    continue
                n3 = -(n1 + n2)
                triple = [n1, n2, n3]
                if n3 in nums_dict and n3 >= n1 and n3 >= n2 and triple.count(n3) <= nums_dict[n3]:
                    result.append(triple)
        return result


if __name__ == '__main__':
    for input_ in [[-1, 0, 1, 2, -1, -4]]:
        solution = Solution().threeSum(input_)
        print(solution)
