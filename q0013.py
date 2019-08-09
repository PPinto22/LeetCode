class Solution:
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        return sum(self.single_roman_to_int(roman, next) for roman, next in self.roman_iterator(s))

    def roman_iterator(self, s):
        for i, roman in enumerate(s):
            yield roman, s[i + 1] if i + 1 < len(s) else None

    def single_roman_to_int(self, roman, next):
        value = Solution.romans[roman]
        if next is not None and Solution.romans[next] > value:
            value *= -1
        return value


if __name__ == '__main__':
    for roman in ['MMMCDLII']:
        result = Solution().romanToInt(roman)
        print(result)
