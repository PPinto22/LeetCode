class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        if x <= 0:
            return True if x == 0 else False

        n_digits = int(math.log10(x)) + 1

        def get_digit(i):
            return (x // 10 ** (n_digits - 1 - i)) % 10

        for i in range((n_digits // 2) + 1):
            digit1 = get_digit(i)
            digit2 = get_digit(n_digits - 1 - i)
            if digit1 != digit2:
                return False
        else:
            return True


if __name__ == '__main__':
    for test_case in [-1, 0, 5, 121, 123, 4545, 4554]:
        result = Solution().isPalindrome(test_case)
        print(result)
