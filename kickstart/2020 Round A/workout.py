import math


def solve(N, K, sessions):
    diffs = [sessions[i + 1] - sessions[i] for i in range(N - 1)]
    return min_binary_search(1, max(diffs), constraints, K, diffs)


# Validate if it is possible to achieve the given difficulty
# with less than 'max_splits' splits
def constraints(difficulty, max_splits, diffs):
    splits = sum(get_splits(diffs, difficulty))
    return splits <= max_splits


# Find the minimum value between lower and upper
# that meets the given constraints
def min_binary_search(lower, upper, constraints, *args):
    while lower <= upper:
        middle = (lower + upper) // 2
        if constraints(middle, *args):
            upper = middle - 1
        else:
            lower = middle + 1
    return lower


# Lists how many additional sessions must be added between
# each session get a the difficulty of 'target' (at most)
def get_splits(diffs, target):
    return [math.ceil(diff / target) - 1 for diff in diffs]


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        # N: Sessions; K: Additional sessions
        N, K = map(int, input().split())
        sessions = list(map(int, input().split()))
        result = solve(N, K, sessions)
        print('Case #{}: {}'.format(Ti, result), flush=True)
