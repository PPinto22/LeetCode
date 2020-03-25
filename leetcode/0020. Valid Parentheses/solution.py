class Solution:

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in self.brackets:
                stack.append(bracket)
            else:
                if not stack or bracket != self.brackets[stack.pop()]:
                    return False
        return not stack


if __name__ == '__main__':
    for input_ in ["({})", "", "{{"]:
        solution = Solution().isValid(input_)
        print(solution)
