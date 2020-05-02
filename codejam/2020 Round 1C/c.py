# FIXME: Time Limit Exceeded

import math
from fractions import Fraction


def solve(n, d, slices):
    slices.sort()
    cuts = math.inf
    tested_sizes = set()
    for size in slices:
        for divisor in range(1, d + 1):
            target_size = Fraction(size, divisor)
            if target_size not in tested_sizes:
                cuts = min(cuts, min_cuts_given_size(n, d, slices, target_size))
                tested_sizes.add(target_size)
    return cuts


def min_cuts_given_size(n, d, slices, target_size):
    cuts = 0
    equal_slices = 0
    for slice in slices:
        missing_slices = d - equal_slices
        if is_fully_usable(missing_slices, slice, target_size):
            new_slices = slice // target_size
            cuts += new_slices - 1
            equal_slices += new_slices
        else:
            new_slices = min(slice // target_size, missing_slices)
            cuts += new_slices
            equal_slices += new_slices
        assert equal_slices <= d
        if equal_slices == d:
            break

    return cuts if equal_slices == d else math.inf


def is_fully_usable(diners, slice_size, target_size):
    return (slice_size % target_size == 0) and (slice_size / target_size <= diners)


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        n, d = map(int, input().split())
        slices = [int(a) for a in input().split()]
        result = solve(n, d, slices)
        print('Case #{}: {}'.format(Ti, result))
