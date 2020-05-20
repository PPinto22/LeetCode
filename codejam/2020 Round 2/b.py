from itertools import chain


def solve(C, D, X, links):
    computers = [Computer(i + 1, x) for (i, x) in chain([(0, 0)], enumerate(X))]
    sort_computers(C, computers)

    latencies = []
    for source, dest in links:
        diff = computers[dest - 1].time - computers[source - 1].time
        latencies.append(abs(diff) if diff != 0 else 1)
    return latencies


def split_computers(computers):
    source, computers_prev, computers_time = None, [], []
    for computer in computers:
        if computer.type == "prev":
            computers_prev.append(computer)
        elif computer.type == "time":
            computers_time.append(computer)
        elif computer.type == "source":
            source = computer
    return source, computers_prev, computers_time


def sort_computers(C, computers):
    source, computers_prev, computers_time = split_computers(computers)

    computers_prev.sort(key=lambda c: c.prev)
    computers_time.sort(key=lambda c: c.time)

    sorted_computers = [source]
    i = j = 0
    for n in range(1, C):
        last = sorted_computers[-1]
        prev = computers_prev[i] if i < len(computers_prev) else None
        time = computers_time[j] if j < len(computers_time) else None
        if prev and prev.prev <= n:
            sorted_computers.append(prev)
            i += 1
            prev.time = last.time if last.prev == prev.prev else last.time + 1
        else:
            sorted_computers.append(time)
            j += 1
            time.prev = last.prev if last.time == time.time else n


class Computer:
    def __init__(self, id, X):
        self.id = id
        self.type = "source" if X == 0 else "time" if X > 0 else "prev"
        self.time = X if X >= 0 else None
        self.prev = -X if X <= 0 else None


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        C, D = map(int, input().split())
        X = [int(xi) for xi in input().split()]
        links = []
        for i in range(D):
            u, v = map(int, input().split())
            links.append((u, v))
        result = solve(C, D, X, links)
        print('Case #{}: {}'.format(Ti, ' '.join(map(str, result))))
