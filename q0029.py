MIN_INT = -2147483648
MAX_INT = 2147483647


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge cases
        if divisor == 0 or (dividend == MIN_INT and divisor == -1):
            return MAX_INT

        # Transform to unsigned int
        sign = int(not (dividend > 0) ^ (divisor > 0)) * 2 - 1
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        # Iterate over each bit of the dividend from left to right
        # (32-bit signed => 31 bits after abs
        for i in range(31, -1, -1):
            dividend_leftmost = dividend >> i
            if divisor <= dividend_leftmost:
                quotient += 1 << i
                remainder = (dividend_leftmost - divisor)
                dividend = dividend - (dividend_leftmost << i) + (remainder << i)

        # remainder = dividend
        # print("Quotient: {}\tRemainder: {}".format(quotient, remainder))

        # FIXME: Multiplication is not allowed
        return quotient * sign


def main():
    def readlines():
        for line in [#"-10", "-3",
                     "-2147483648", "1"
                     ]:
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            dividend = int(line);
            line = next(lines)
            divisor = int(line);

            ret = Solution().divide(dividend, divisor)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
