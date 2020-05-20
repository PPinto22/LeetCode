import math


def solve(l, r):
    left, right = Tower(l), Tower(r)
    high, low = sort(left, right)

    # phase 1
    phase1_clients = get_first_phase_clients(high.n - low.n)
    high.n -= get_first_fase_pancakes(phase1_clients)

    # phase 2
    high, low = sort(left, right)

    phase2_clients_high = get_second_phase_clients(phase1_clients, high.n)
    high.n -= get_second_fase_pancakes(phase1_clients, phase2_clients_high)

    phase2_clients_low = get_second_phase_clients(phase1_clients + 1, low.n)
    low.n -= get_second_fase_pancakes(phase1_clients + 1, phase2_clients_low)

    return phase1_clients + phase2_clients_high + phase2_clients_low, left.n, right.n


def sort(left, right):
    if left.n >= right.n:
        return left, right
    else:
        return right, left


# Note: These don't work due to rounding errors. Do binary search instead
# def get_first_phase_clients(pancakes):
#     return math.floor((-1 + math.sqrt(1 + 8 * pancakes)) / 2)
# def get_second_phase_clients(previous_clients, pancakes):
#     return math.floor((-previous_clients + math.sqrt(previous_clients ** 2 + 4 * pancakes)) / 2)


def binary_search_clients(pancakes, f):
    low, high = 0, pancakes
    while low < high:
        mid = math.ceil((low + high) / 2)
        mid_pancakes = f(mid)
        if mid_pancakes > pancakes:
            high = mid - 1
        else:
            low = mid
    return low


def get_first_phase_clients(pancakes):
    return binary_search_clients(pancakes, lambda n: get_first_fase_pancakes(n))


def get_first_fase_pancakes(clients):
    return clients * (clients + 1) // 2


def get_second_phase_clients(previous_clients, pancakes):
    return binary_search_clients(pancakes, lambda n: get_second_fase_pancakes(previous_clients, n))


def get_second_fase_pancakes(start, clients):
    return start * clients + clients ** 2


class Tower:
    def __init__(self, n):
        self.n = n


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        L, R = map(int, input().split())
        n, l, r = solve(L, R)
        print('Case #{}: {} {} {}'.format(Ti, n, l, r))
