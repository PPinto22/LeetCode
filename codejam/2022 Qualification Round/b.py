from dataclasses import dataclass

INK_PER_D = int(1e6)
N_PRINTERS = 3


@dataclass
class InkLevels:
    cyan: int = 0
    magenta: int = 0
    yellow: int = 0
    black: int = 0

    def as_tuple(self):
        return self.cyan, self.magenta, self.yellow, self.black

    def sum(self):
        return sum(self.as_tuple())


@dataclass
class Solution(InkLevels):
    possible: bool = None

    @staticmethod
    def from_ink_levels(ink_levels: InkLevels):
        return Solution(possible=True, *ink_levels.as_tuple())


def solve(printers: [InkLevels]):
    cyan_per_printer = [p.cyan for p in printers]
    magenta_per_printer = [p.magenta for p in printers]
    yellow_per_printer = [p.yellow for p in printers]
    black_per_printer = [p.black for p in printers]

    candidate_color = InkLevels(cyan=min(cyan_per_printer), magenta=min(magenta_per_printer),
                                yellow=min(yellow_per_printer), black=min(black_per_printer))

    if candidate_color.sum() < INK_PER_D:
        return Solution(possible=False)

    excess_ink = candidate_color.sum() - INK_PER_D

    cyan_to_remove = min(candidate_color.cyan, excess_ink)
    excess_ink -= cyan_to_remove
    candidate_color.cyan -= cyan_to_remove

    magenta_to_remove = min(candidate_color.magenta, excess_ink)
    excess_ink -= magenta_to_remove
    candidate_color.magenta -= magenta_to_remove

    yellow_to_remove = min(candidate_color.yellow, excess_ink)
    excess_ink -= yellow_to_remove
    candidate_color.yellow -= yellow_to_remove

    black_to_remove = min(candidate_color.black, excess_ink)
    excess_ink -= black_to_remove
    candidate_color.black -= black_to_remove

    return Solution.from_ink_levels(candidate_color)


def main():
    test_cases = int(input())
    for case_i in range(1, test_cases + 1):
        printers = [InkLevels(*map(int, input().split())) for _ in range(N_PRINTERS)]
        solution = solve(printers)
        if solution.possible:
            print(f'Case #{case_i}: {solution.cyan} {solution.magenta} {solution.yellow} {solution.black}')
        else:
            print(f'Case #{case_i}: IMPOSSIBLE')


if __name__ == '__main__':
    main()
