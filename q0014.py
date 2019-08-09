from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        length = min(len(s) for s in strs) if strs else 0
        for i in range(0, length):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                return prefix
        return prefix


if __name__ == '__main__':
    for input_ in [["dog", "racecar", "car"], ["flower", "flow", "flight"]]:
        result = Solution().longestCommonPrefix(input_)
        print(result)
