def solve(N, activities):
    solution = [None] * N
    partners = ['J', 'C']
    free_at = {partner: 0 for partner in partners}
    sorted_indexes = sorted(range(N), key=lambda i: activities[i])
    for i in sorted_indexes:
        start, end = activities[i]
        free_partners = [partner for partner in partners
                         if free_at[partner] <= start]
        if not free_partners:
            return 'IMPOSSIBLE'

        partner = free_partners[0]
        free_at[partner] = end
        solution[i] = partner
    return ''.join(solution)


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        N = int(input())
        activities = [list(map(int, input().split())) for i in range(N)]
        result = solve(N, activities)
        print('Case #{}: {}'.format(Ti, result))
