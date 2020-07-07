from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        missing = defaultdict(int)
        for c in t:
            missing[c] += 1
        best = ""
        left, right = 0, -1

        def is_valid():
            return all(missing[x] < 1 for x in missing)

        def expand():
            nonlocal right
            assert right <= n
            right += 1
            if right < n and s[right] in missing:
                missing[s[right]] -= 1

        def shrink():
            nonlocal left
            assert left <= right
            if s[left] in missing:
                missing[s[left]] += 1
            left += 1

        while right < n:
            if is_valid() and left <= right:
                if not best or (right - left + 1) < len(best):
                    best = s[left:right + 1]
                shrink()
            else:
                expand()

        return best


if __name__ == '__main__':
   print(Solution().minWindow("ADOBECODEBANC", "ABC"))