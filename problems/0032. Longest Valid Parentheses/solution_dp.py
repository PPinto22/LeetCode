class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp[i] = longest valid parentheses ending at position i
        # if s[i] == '(' then dp[i] = 0, because no string ending with an open parentheses is valid
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    previous_length = dp[i - 2] if (i - 2) >= 0 else 0
                    dp[i] = 2 + previous_length
                else:
                    previous_length = dp[i - 1]
                    dp[i] = 2 + previous_length + dp[i - previous_length - 2] \
                        if (i - previous_length - 1) >= 0 and s[i - previous_length - 1] == '(' else 0
        return max(dp, default=0)


def stringToString(input):
    import json

    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().longestValidParentheses(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
