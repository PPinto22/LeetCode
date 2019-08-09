class Solution:
    romans = [
        ['I', 'V'],
        ['X', 'L'],
        ['C', 'D'],
        ['M']
    ]

    def intToRoman(self, num: int) -> str:
        return ''.join(roman for roman in
                       (self.get_roman(order, digit) for order, digit in self.get_number_orders(num)))

    def get_number_orders(self, num):
        num_str = str(num)
        for i, digit in enumerate(num_str):
            yield len(num_str) - 1 - i, int(digit)

    def get_roman(self, order, digit):
        if digit == 0:
            return ''
        elif digit <= 3:
            return Solution.romans[order][0] * digit
        elif digit == 4:
            return Solution.romans[order][0] + Solution.romans[order][1]
        elif digit <= 8:
            return Solution.romans[order][1] + Solution.romans[order][0] * (digit - 5)
        elif digit == 9:
            return Solution.romans[order][0] + Solution.romans[order+1][0]
        else:
            raise AttributeError("Invalid digit: " + str(digit))


if __name__ == '__main__':
    for num in [3452]:
        result = Solution().intToRoman(num)
        print(result)
