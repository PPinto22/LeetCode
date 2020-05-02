def solve(x, y, m):
    peppurr_positions = get_peppurr_positions(x, y, m)
    for i, position in enumerate(peppurr_positions):
        if can_reach(i, position):
            return i
    return 'IMPOSSIBLE'

def can_reach(moves, position):
    return abs(position[0]) + abs(position[1]) <= moves

def get_peppurr_positions(x, y, m):
    position = (x, y)
    positions = [position]
    for move in m:
        (x, y) = position
        if move == 'N':
            position = (x, y+1)
        elif move == 'E':
            position = (x+1, y)
        elif move == 'S':
            position = (x, y-1)
        elif move == 'W':
            position = (x-1, y)
        positions.append(position)
    return positions


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        line = input().split()
        x, y, m = int(line[0]), int(line[1]), line[2]
        result = solve(x, y, m)
        print('Case #{}: {}'.format(Ti, result))
