# FIXME: Runtime Error on both test cases


def solve(N, K, P, stacks):
    sum_ = cumulative_sum(stacks)
    # dp[i][j]: maximum sum that can be obtained using the first i stacks
    # when we need to pick j plates in total. Note: j starts at 0
    dp = init_dp(N, P, sum_)
    for i in range(1, N):
        for j in range(1, P + 1):
            # x: number of plates to pick from stack i
            for x in range(min(j, K) + 1):
                # Pick (j-x) plates from previous stacks and x plates from current stack
                score = dp[i - 1][j - x] + sum_[i][x]
                dp[i][j] = max(dp[i][j], score)
    return dp[N - 1][P]


def init_dp(N, P, sum_):
    dp = [[0 for i in range(P + 1)] for j in range(N)]
    for i, value in enumerate(sum_[0]):
        dp[0][i] = value
    return dp


# Cumulative sum, starting at 0. E.g:
# cumulative_sum([1, 2, 3]) = [0, 1, 3, 6]
def cumulative_sum(stacks):
    sum_ = []
    for stack in stacks:
        stack_sum = [0]
        for i in range(len(stack)):
            stack_sum.append(stack_sum[i] + stack[i])
        sum_.append(stack_sum)
    return sum_


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        # N: Stacks; K: Plates per stack; P: Total plates
        N, K, P = map(int, input().split())
        stacks = [list(map(int, input().split())) for _ in range(N)]
        result = solve(N, K, P, stacks)
        print('Case #{}: {}'.format(Ti, result), flush=True)
