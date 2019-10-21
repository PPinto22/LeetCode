# Knuth–Morris–Pratt(KMP) Pattern Matching
# From https://www.youtube.com/watch?v=GTJr8OvyEVQ


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        kmp = self.getKMPArray(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = kmp[j - 1]
                else:
                    i += 1
        if j == len(needle):
            return i - len(needle)
        else:
            return -1

    def getKMPArray(self, pattern):
        kmp = [0] * len(pattern)
        j = 0
        i = 1
        while i < len(pattern):
            if pattern[j] == pattern[i]:
                kmp[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = kmp[j - 1]
                else:
                    # kmp[i] = 0 (NOP because value is already 0)
                    i += 1
        return kmp


def main():
    def readlines():
        for line in ["mississippi", "issip"]:
            yield line

    lines = readlines()
    while True:
        try:
            haystack = next(lines)
            needle = next(lines)

            ret = Solution().strStr(haystack, needle)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
