from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest_diff = target - sum(nums[:3])
        nums.sort()

        for i in range(0, len(nums) - 2):
            n1 = nums[i]
            if i > 0 and nums[i - 1] == n1:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                n2 = nums[left]
                n3 = nums[right]
                sum_ = n1 + n2 + n3
                diff = target - sum_
                smallest_diff = diff if abs(diff) < abs(smallest_diff) else smallest_diff
                if diff > 0:
                    left += 1
                    while left < right and nums[left] == n2:
                        left += 1
                elif diff < 0:
                    right -= 1
                    while right > left and nums[right] == n3:
                        right -= 1
                else:
                    return target

        return target - smallest_diff


if __name__ == '__main__':
    for input_ in [[-1, 2, 1, -4]]:
        solution = Solution().threeSumClosest(input_, target=1)
        print(solution)
