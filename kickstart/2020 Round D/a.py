import math


def solve(n, visitors):
    prev_max = -math.inf
    record_breaks = 0
    for i, v in enumerate(visitors):
        if v > prev_max and (i == n-1 or v > visitors[i+1]):
            record_breaks += 1
        prev_max = max(prev_max, v)
    return record_breaks


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T+1):
        n = int(input())
        visitors = list(map(int, input().split()))
        result = solve(n, visitors)
        print('Case #{}: {}'.format(Ti, result))
