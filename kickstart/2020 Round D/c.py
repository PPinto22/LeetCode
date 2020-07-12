def solve(n, a, b, parents, children):
    visits_a, visits_b = [0] * (n + 1), [0] * (n + 1)

    # NOTE: DFS couldn't be recursive because of stack overflow (RE)
    visited = [False] * (n + 1)
    stack = [1]
    path = []
    while stack:
        cur = stack[-1]
        has_children = bool(children[cur])
        visited_children = not children[cur] or visited[children[cur][0]]

        if not has_children or not visited_children:
            path.append(cur)
            for child in children[cur]:
                stack.append(child)

        if not has_children or visited_children:
            stack.pop()
            path.pop()
            visited[cur] = True
            visits_a[cur] += 1
            visits_b[cur] += 1
            if len(path) >= a:
                prev = path[-a]
                visits_a[prev] += visits_a[cur]
            if len(path) >= b:
                prev = path[-b]
                visits_b[prev] += visits_b[cur]

    prob_a = [va / n for va in visits_a]
    prob_b = [vb / n for vb in visits_b]
    return sum(prob_a[i] + prob_b[i] - (prob_a[i] * prob_b[i]) for i in range(n + 1))


def build_children(n, parents):
    children = [[] for _ in range(n + 1)]
    for i, p in enumerate(parents):
        children[p].append(i + 2)
    return children


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        n, a, b = map(int, input().split())
        parents = [int(x) for x in input().split()]
        children = build_children(n, parents)
        result = solve(n, a, b, parents, children)
        print('Case #{}: {}'.format(Ti, result))
