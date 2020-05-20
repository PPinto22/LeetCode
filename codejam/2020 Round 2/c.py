# FIXME: This is a brute-force solution which only works for Test Set 1.
#  Getting Memory Limit Exceeded in Test Set 2 when trying to generate all possible combinations of wormhole pairs

import math


def solve(N, holes):
    directions = get_directions(N, holes)
    wormhole_combinations = [wormhole_list_to_map(wormholes) for wormholes in get_wormhole_combinations(holes)]
    answer = 0
    for direction in directions:
        lines = get_lines(holes, direction)
        for start in holes:
            for wormholes in wormhole_combinations:
                answer = max(answer, simulate(start, direction, wormholes, lines))

    return answer


def simulate(start, direction, wormholes, lines):
    visited = set()
    wormhole_arrivals = set()
    current = start
    wormhole = False  # whether the ball arrived at 'current' via a wormhole or not
    while current:
        visited.add(current)

        if wormhole:
            current_i = lines[current].index(current)
            next_ = lines[current][current_i + 1] \
                if current_i + 1 < len(lines[current]) else None
            wormhole = False
        elif current in wormholes:
            next_ = wormholes[current]
            if next_ in wormhole_arrivals:
                break  # infinite loop!
            wormhole_arrivals.add(next_)
            wormhole = True
        else:
            next_ = None
            wormhole = False

        current = next_

    return len(visited)


def wormhole_list_to_map(wormholes):
    wormhole_map = {}
    for p1, p2 in wormholes:
        wormhole_map[p1] = p2
        wormhole_map[p2] = p1
    return wormhole_map


def get_lines(holes, direction):
    lines = {}
    visited = set()
    for source in holes:
        if source in visited:
            continue
        visited.add(source)
        line = [source]
        for dest in holes:
            if dest in visited:
                continue
            dx, dy = dest[0] - source[0], dest[1] - source[1]
            if dx * direction[1] == dy * direction[0]:
                line.append(dest)
                visited.add(dest)
        line.sort(reverse=direction[0] < 0 or (direction[0] == 0 and direction[1] < 0))
        for point in line:
            lines[point] = line
    return lines


def get_wormhole_combinations(holes):
    combinations = []

    def dfs(available, build):
        nonlocal combinations
        if len(available) < 2:
            combinations.append(build)
            return

        dfs(available[1:], build)
        for j in range(1, len(available)):
            dfs(available[1:j] + available[j + 1:], build + [(available[0], available[j])])

    dfs(holes, [])
    return combinations


def get_directions(N, holes):
    if len(holes) < 2:
        return {(1, 1)}

    directions = set()
    for i in range(N - 1):
        p1 = holes[i]
        for j in range(i + 1, N):
            p2 = holes[j]
            vector = get_vector(p1, p2)
            if vector not in directions:
                directions.add(vector)
    return directions


def get_vector(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    gcd = math.gcd(dx, dy)
    return dx // gcd, dy // gcd


def main():
    T = int(input())
    for Ti in range(1, T + 1):
        N = int(input())
        holes = []
        for i in range(N):
            x, y = map(int, input().split())
            holes.append((x, y))
        result = solve(N, holes)
        print('Case #{}: {}'.format(Ti, result))


if __name__ == '__main__':
    main()
