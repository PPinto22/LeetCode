from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        def buildCombinations(s='', left=0, right=0):
            if len(s) == 2 * n:
                combinations.append(s)
                return
            if left < n:
                buildCombinations(s+'(', left+1, right)
            if left > right:
                buildCombinations(s+')', left, right+1)

        buildCombinations()
        return combinations


if __name__ == '__main__':
    for input_ in [3, 4]:
        solution = Solution().generateParenthesis(input_)
        print(solution)
