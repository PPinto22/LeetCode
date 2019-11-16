from typing import List


class Solution:
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []

        def explore(combination):
            i = len(combination)
            if i == len(digits):
                combinations.append(''.join(combination))
            else:
                for letter in Solution.phone[digits[i]]:
                    new_combination = combination + [letter]
                    explore(new_combination)

        if digits:
            explore([])

        return combinations



if __name__ == '__main__':
    for input_ in ["23"]:
        result = Solution().letterCombinations(input_)
        print(result)
