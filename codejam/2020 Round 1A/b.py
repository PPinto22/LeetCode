# def build_pascal(N):
#     pascal = [[1]]
#     for r in range(1, N):
#         middle = [pascal[r - 1][k - 1] + pascal[r - 1][k] for k in range(1, r)]
#         pascal.append([1] + middle + [1])
#     return pascal


def reverse_binary(N):
    return [1 if digit == '1' else 0 for digit in reversed(bin(N)[2:])]


def solve(N):
    if N < DEPTH:
        return [(i, 1) for i in range(1, N + 1)]

    path = []
    target = N - DEPTH
    target_rows = reverse_binary(target)
    direction = 1  # 1: left -> right; -1: right -> left
    for r in range(DEPTH):
        k = 0 if direction == 1 else r
        if r < len(target_rows) and target_rows[r] == 1:
            for i in range(r + 1):
                path.append((r + 1, k + direction * i + 1))
            direction *= -1
        else:
            path.append((r + 1, k + 1))

    # Pick up an extra "1" for every row that was traversed
    for i in range(sum(target_rows)):
        k = 0 if direction == 1 else DEPTH + i
        path.append((DEPTH + i + 1, k + 1))

    return path


# 30 is the minimum power of 2 that fits test case 3 (10^9)
DEPTH = 30
# pascal = build_pascal(DEPTH)

if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        N = int(input())
        result = solve(N)
        print('Case #{}:'.format(Ti))
        for (row, col) in result:
            print('{} {}'.format(row, col))