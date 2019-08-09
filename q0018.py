from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            n1 = nums[i]
            if i > 0 and nums[i - 1] == n1:
                continue
            for j in range(i + 1, len(nums) - 2):
                n2 = nums[j]
                if j > i + 1 and nums[j - 1] == n2:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    n3 = nums[left]
                    n4 = nums[right]
                    sum_ = n1 + n2 + n3 + n4
                    diff = target - sum_
                    if diff == 0:
                        solutions.append([n1, n2, n3, n4])
                    if diff >= 0:
                        left += 1
                        while left < right and nums[left] == n3:
                            left += 1
                    if diff <= 0:
                        right -= 1
                        while right > left and nums[right] == n4:
                            right -= 1
        return solutions


if __name__ == '__main__':
    for input_ in [[-1, 0, -5, -2, -2, -4, 0, 1, -2]]:
        solution = Solution().fourSum(input_, target=-9)
        print(solution)
