from __future__ import annotations


def solve(dice_sides: list[int]):
    # straight always starts at 1
    straight_end = 1

    sorted_dice = iter(sorted(dice_sides))
    next(sorted_dice)  # Skip the first die as it is always used to start the straight at 1
    for die_sides in sorted_dice:
        if die_sides > straight_end:
            straight_end += 1

    return straight_end


def main():
    test_cases = int(input())
    for case_i in range(1, test_cases + 1):
        n_dice = int(input())
        dice_sides = [int(si) for si in input().split()]
        solution = solve(dice_sides)
        print(f'Case #{case_i}: {solution}')


if __name__ == '__main__':
    main()
