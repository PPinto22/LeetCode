class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(length, max_length)
        return max_length


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
