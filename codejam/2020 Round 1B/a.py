def solve(x, y):
    if count_even([x, y]) != 1:
        return 'IMPOSSIBLE'
    jumps = []
    while x != 0 or y != 0:
        if x % 2 == 1:
            # move East or West
            if correct_move((x, y), ((x - 1) // 2, y // 2)) == 1:
                x -= 1
                jumps.append('E')
            else:
                x += 1
                jumps.append('W')
        else:
            # move North or South
            if correct_move((x, y), (x // 2, (y - 1) // 2)) == 1:
                y -= 1
                jumps.append('N')
            else:
                y += 1
                jumps.append('S')
        x //= 2
        y //= 2
    return ''.join(jumps)


def correct_move(from_, to):
    # If 'to' is the target, it's always correct
    if to[0] == 0 and to[1] == 0:
        return True
    # If we're one step away from the target, 'to' must be the target
    if sum(abs(x) for x in from_) == 1 and sum(abs(x) for x in to) != 0:
        return False

    # General case: there must be one odd and even number at all times
    return count_even(to) == 1


def count_even(list_):
    return sum(1 if a % 2 == 1 else 0 for a in list_)


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        X, Y = map(int, input().split())
        result = solve(X, Y)
        print('Case #{}: {}'.format(Ti, result))
