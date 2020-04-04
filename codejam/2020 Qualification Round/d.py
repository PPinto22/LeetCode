from typing import Union, List, Tuple, Optional


def solve(B):
    def set(index, value):
        nonlocal control_equal, control_complement, known

        # Fix to prevent unpaired bits right before a fluctuation
        if (not control_complement or not control_equal) \
                and (query % 10 == 0) \
                and (known % 2 == 0):
            return

        solution[index] = value
        known += 1
        pair = get_pair(index)
        if not control_equal and value == pair[1]:
            control_equal = pair
        elif not control_complement \
                and pair[1] is not None \
                and value != pair[1]:
            control_complement = pair

    def get_pair(index):
        pair_index = B - 1 - index
        return [pair_index, solution[pair_index]]

    def determine_fluctuation():
        nonlocal control_complement, control_equal
        possibilities = ['complement', 'reverse', 'both', 'none']
        if control_equal:
            index, old = control_equal
            new = ask(index)
            if old == new:
                possibilities = [p for p in possibilities if p in {'reverse', 'none'}]
            else:
                possibilities = [p for p in possibilities if p in {'complement', 'both'}]
            control_equal = index, new
        if control_complement:
            index, old = control_complement
            new = ask(index)
            if old == new:
                possibilities = [p for p in possibilities if p in {'both', 'none'}]
            else:
                possibilities = [p for p in possibilities if p in {'complement', 'reverse'}]
            control_complement = index, new
        return possibilities[0]

    def apply_fluctuation(fluctuation):
        def complement():
            for i in range(B):
                if solution[i] is not None:
                    solution[i] = not solution[i]

        if fluctuation == 'complement':
            complement()
        elif fluctuation == 'reverse':
            solution.reverse()
        elif fluctuation == 'both':
            complement()
            solution.reverse()

    def ask(i):
        nonlocal query
        query += 1
        print(i + 1, flush=True)
        response = input()
        return True if response == '1' else False

    def next_index():
        return (known // 2) if (known % 2 == 0) else (B - (known // 2) - 1)

    solution: List[Union[bool, None]] = [None] * B
    control_equal: Optional[Tuple[int, bool]] = None
    control_complement: Optional[Tuple[int, bool]] = None
    query = 0
    known = 0

    while known < B and query < 150:
        if query > 0 and query % 10 == 0:
            fluctuation = determine_fluctuation()
            apply_fluctuation(fluctuation)
        else:
            index = next_index()
            set(index, ask(index))

    return ''.join(map(lambda x: '1' if x else '0', solution))


if __name__ == '__main__':
    T, B = map(int, input().split())
    for Ti in range(1, T + 1):
        solution = solve(B)
        print(solution, flush=True)
        if input() == 'N':
            break
