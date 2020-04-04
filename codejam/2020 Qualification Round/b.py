def solve(S):
    result = ''
    depth = 0

    for c in S:
        value = int(c)
        for i in range(depth, value):
            result += '('
            depth += 1
        for i in range(value, depth):
            result += ')'
            depth -= 1
        result += c

    for i in range(0, depth):
        result += ')'
        depth -= 1

    return result


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        S = input()
        result = solve(S)
        print('Case #{}: {}'.format(Ti, result))
