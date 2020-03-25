import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        centers = [i * 0.5 for i in range(2 * len(s))]
        palindromes = [self.longestPalindromeAtCenter(s, center) for center in centers]
        longest_palindrome = max(palindromes, key=lambda x: len(x), default="")
        return longest_palindrome

    def longestPalindromeAtCenter(self, s, center):
        if center.is_integer():
            center = int(center)
            lower = center - 1
            upper = center + 1
            palind = s[center]
        else:
            lower = math.floor(center)
            upper = math.ceil(center)
            palind = ""

        while lower >= 0 and upper < len(s) and s[lower] == s[upper]:
            palind = s[lower] + palind + s[upper]
            lower -= 1
            upper += 1

        return palind