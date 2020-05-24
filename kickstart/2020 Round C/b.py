def solve(R, C, wall):
    dependencies = build_dependencies(R, C, wall)
    try:
        order = topological_sort(dependencies)
        return ''.join(order)
    except ValueError:
        return -1


def topological_sort(dependencies):
    order = []
    visited = set()

    def dfs(current, wip):
        if current in wip:
            raise ValueError
        if current in visited:
            return

        wip.add(current)
        visited.add(current)

        for dependency in dependencies[current]:
            dfs(dependency, wip)
        order.append(current)
        wip.remove(current)

    for node in dependencies:
        dfs(node, set())

    return order


def build_dependencies(R, C, wall):
    dependencies = {}
    for i in range(R):
        for j in range(C):
            top = wall[i][j]
            bottom = wall[i + 1][j] if i + 1 < R else top
            for x in [top, bottom]:
                if x not in dependencies:
                    dependencies[x] = set()
            if top != bottom:
                dependencies[top].add(bottom)
    return dependencies


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        R, C = map(int, input().split())
        wall = []
        for row in range(R):
            wall.append(list(input()))
        result = solve(R, C, wall)
        print('Case #{}: {}'.format(Ti, result))
