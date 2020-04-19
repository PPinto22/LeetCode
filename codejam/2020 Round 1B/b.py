from random import randint
import math


class LuckyGuessException(Exception):
    pass


class OutOfTriesException(Exception):
    pass


class WrongAnswerException(Exception):
    pass


class Solver:
    def __init__(self, A, B):
        self.WALL_SIZE = 1e9
        self.A = A
        self.B = B
        self.tries = 0
        self.center = None

    def solve(self):
        try:
            self._solve()
        except LuckyGuessException:
            return True
        except OutOfTriesException:
            return False
        except WrongAnswerException:
            return False

    def _solve(self):
        # Find a point (p1) inside the circle
        p1 = self.find_hit()

        # Extending from p1, find the edges of the circle
        p2 = self.find_edge(p1, [1, 0])  # edge 1
        p3 = self.find_edge(p1, [-1, 0])  # edge 2
        p4 = Solver.middle(p2, p3)  # middle point between p2 and p3

        v1 = Solver.normalize(Solver.subtract(p3, p2))  # vector p2 -> p3
        v2 = Solver.perpendicular(v1)  # perpendicular of v1 (passes through the center)

        p5 = self.find_edge(p4, v2)  # edge 1
        p6 = self.find_edge(p4, Solver.inverse(v2))  # edge 2

        center = Solver.middle(p5, p6)
        # if the answer is correct, this will stop the execution
        self.throw_dart(center)

        # if we get here, the answer was wrong :(
        raise WrongAnswerException

    def find_edge(self, point, direction):
        l = 0
        r = 2 * max(self.A, self.B)
        while l < r:
            m = (l + r) // 2
            true_middle = self.add(point, Solver.multiply(m, direction))
            feedback = self.throw_dart(true_middle)
            if feedback == 'HIT':
                l = m + 1
            else:
                r = m
        return self.add(point, Solver.multiply(l - 1, direction))

    def find_hit(self):
        while True:
            p1 = (randint(-A, A), randint(-B, B))
            feedback = self.throw_dart(p1)
            if feedback == 'HIT':
                return p1

    def throw_dart(self, point):
        if self.tries > 300:
            raise OutOfTriesException
        self.tries += 1

        print('{} {}'.format(point[0], point[1]))
        feedback = input()
        if feedback == 'CENTER':
            self.center = point
            raise LuckyGuessException
        return feedback

    def add(self, point, vector):
        px = round(max(-self.WALL_SIZE, min(self.WALL_SIZE, point[0] + vector[0])))
        py = round(max(-self.WALL_SIZE, min(self.WALL_SIZE, point[1] + vector[1])))
        return px, py

    @staticmethod
    def normalize(vector):
        magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        return vector[0] / magnitude, vector[1] / magnitude

    @staticmethod
    def subtract(p1, p2):
        return p1[0] - p2[0], p1[1] - p2[1]

    @staticmethod
    def multiply(scalar, vector):
        return scalar * vector[0], scalar * vector[1]

    @staticmethod
    def perpendicular(vector):
        return -vector[1], vector[0]

    @staticmethod
    def inverse(vector):
        return -vector[0], -vector[1]

    @staticmethod
    def middle(p1, p2):
        return (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2


if __name__ == '__main__':
    T, A, B = map(int, input().split())
    for Ti in range(1, T + 1):
        result = Solver(A, B).solve()
