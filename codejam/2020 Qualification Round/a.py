def trace(N, matrix):
    return sum(matrix[i][i] for i in range(N))


def repeats(N, matrix, axis):
    count = 0
    for i in range(N):
        vector = matrix[i] if axis == 'rows' else [matrix[row][i] for row in range(N)]
        has_repeats = len(vector) > len(set(vector))
        if has_repeats:
            count += 1
    return count


def solve(N, matrix):
    return trace(N, matrix), repeats(N, matrix, 'rows'), repeats(N, matrix, 'columns')


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        # N: matrix size
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        k, r, c = solve(N, matrix)
        print('Case #{}: {} {} {}'.format(Ti, k, r, c))
