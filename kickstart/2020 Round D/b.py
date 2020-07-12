def solve(n, notes):
    unique_notes = [notes[i] for i in range(n) if i == 0 or notes[i-1] != notes[i]]
    m = len(unique_notes)
    up = down = violations = 0
    for i in range(1, m):
        if unique_notes[i] > unique_notes[i-1]:
            up += 1
            down = 0
        else:
            down += 1
            up = 0
        if up == 4 or down == 4:
            violations += 1
            up = down = 0
    return violations


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        n = int(input())
        notes = list(map(int, input().split()))
        result = solve(n, notes)
        print('Case #{}: {}'.format(Ti, result))
