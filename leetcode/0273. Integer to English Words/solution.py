class Solution:
    SCALES = [
        (int(1e9), "Billion"),
        (int(1e6), "Million"),
        (int(1e3), "Thousand"),
        (int(1e2), "Hundred")
    ]

    BASE_NUMBERS = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
    }

    TENS = {
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
    }

    def get_scale(self, num):
        return next(scale for scale in Solution.SCALES if scale[0] <= num)

    def numberToWords(self, num: int) -> str:
        if num < 20:
            return Solution.BASE_NUMBERS[num]
        if num < 100:
            tens = num // 10
            remainder = num % 10
            return Solution.TENS[tens * 10] + ((" " + Solution.BASE_NUMBERS[remainder]) if remainder > 0 else "")

        scale, scale_name = self.get_scale(num)
        qty = num // scale
        remainder = num - (qty * scale)
        return "{} {}".format(self.numberToWords(qty), scale_name) + \
               ((" " + self.numberToWords(remainder)) if remainder > 0 else "")


if __name__ == '__main__':
    solver = Solution()
    print(solver.numberToWords(0))
    print(solver.numberToWords(123))
    print(solver.numberToWords(12345))
    print(solver.numberToWords(1234567))
    print(solver.numberToWords(1234567891))

