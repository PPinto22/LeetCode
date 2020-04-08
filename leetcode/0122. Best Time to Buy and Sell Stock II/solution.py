from typing import List
import json


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, peak, valley = 0, 0, 0
        for i in range(len(prices)):
            if (i + 1 < len(prices) and prices[i + 1] >= prices[i]) and (i == 0 or prices[i - 1] > prices[i]):
                valley = prices[i]
            elif (i > 0 and prices[i - 1] <= prices[i]) and (i + 1 == len(prices) or prices[i + 1] < prices[i]):
                peak = prices[i]
                profit += peak - valley
        return profit


def stringToIntegerList(input):
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
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
