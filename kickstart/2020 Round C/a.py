def solve(N, K, numbers):
    count = 0
    i = 0
    while i < N-K+1:
        start = i
        for i in range(i, i + K):
            if K - numbers[i] != i - start:
                break
        else:
            count += 1
        i = max(i, start + 1)

    return count

def main():
    T = int(input())
    for Ti in range(1, T + 1):
        N, K = map(int, input().split())
        numbers = [int(a) for a in input().split()]
        result = solve(N, K, numbers)
        print('Case #{}: {}'.format(Ti, result))


if __name__ == '__main__':
    main()
