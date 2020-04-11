# FIXME Time Limit Exceeded on Test set 2


def avg(l):
    return sum(l) / len(l) if l else 0


def opposite_of(direction):
    if direction == "up":
        return "down"
    if direction == "down":
        return "up"
    if direction == "left":
        return "right"
    if direction == "right":
        return "left"


class Dancer:
    def __init__(self, row, col, skill):
        self.row = row
        self.col = col
        self.skill = skill
        self.alive = True
        self.neighbor_up = None
        self.neighbor_down = None
        self.neighbor_left = None
        self.neighbor_right = None

    def get_neighbors(self):
        return [neighbor for neighbor in [self.neighbor_up, self.neighbor_down, self.neighbor_left, self.neighbor_right]
                if neighbor]

    def get_neighbor(self, direction):
        if direction == "up":
            return self.neighbor_up
        if direction == "down":
            return self.neighbor_down
        if direction == "left":
            return self.neighbor_left
        if direction == "right":
            return self.neighbor_right

    def set_neighbor(self, direction, neighbor):
        if direction == "up":
            self.neighbor_up = neighbor
        if direction == "down":
            self.neighbor_down = neighbor
        if direction == "left":
            self.neighbor_left = neighbor
        if direction == "right":
            self.neighbor_right = neighbor


class Competition:
    def __init__(self, R, C, skills):
        self.R = R
        self.C = C
        self.round = 0
        self.interest = 0
        self.floor = []
        self.dancers = set()
        for i in range(R):
            self.floor.append([])
            for j in range(C):
                dancer = Dancer(i, j, skills[i][j])
                self.floor[i].append(dancer)
                self.dancers.add(dancer)
        for i in range(R):
            for j in range(C):
                dancer = self.floor[i][j]
                dancer.neighbor_up = self.floor[i - 1][j] if i - 1 >= 0 else None
                dancer.neighbor_down = self.floor[i + 1][j] if i + 1 < R else None
                dancer.neighbor_left = self.floor[i][j - 1] if j - 1 >= 0 else None
                dancer.neighbor_right = self.floor[i][j + 1] if j + 1 < C else None

    def simulate(self):
        elimination_list = []
        while elimination_list or self.round == 0:
            elimination_list.clear()
            self.round += 1
            for dancer in self.dancers:
                self.interest += dancer.skill
                neighbors = dancer.get_neighbors()
                if dancer.skill < avg([neighbor.skill for neighbor in neighbors]):
                    elimination_list.append(dancer)

            elimination_list.sort(key=lambda dancer: (dancer.row, dancer.col))
            for dancer in elimination_list:
                dancer.alive = False
                self.dancers.remove(dancer)
            for dancer in elimination_list:
                for direction in ["up", "down", "left", "right"]:
                    neighbor = dancer.get_neighbor(direction)
                    if neighbor:
                        opposite_direction = opposite_of(direction)
                        neighbor.set_neighbor(opposite_direction, dancer.get_neighbor(opposite_direction))


def solve(R, C, skills):
    competition = Competition(R, C, skills)
    competition.simulate()
    return competition.interest


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        R, C = map(int, input().split())
        skills = [[int(s) for s in input().split()] for row in range(R)]
        result = solve(R, C, skills)
        print('Case #{}: {}'.format(Ti, result))
