def solve(N, patterns):
    splits = [p.split('*') for p in patterns]
    prefixes = [s[0] for s in splits]
    suffixes = [s[-1] for s in splits]
    middle_words = [s[1:len(s) - 1] for s in splits]
    longest_prefix = max(prefixes, key=lambda p: len(p))
    longest_suffix = max(suffixes, key=lambda p: len(p))

    if not all(longest_prefix.startswith(p) for p in prefixes) \
            or not all(longest_suffix.endswith(p) for p in suffixes):
        return '*'

    return ''.join([longest_prefix] + sum(middle_words, []) + [longest_suffix])


if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        N = int(input())
        patterns = [input() for _ in range(N)]
        result = solve(N, patterns)
        print('Case #{}: {}'.format(Ti, result))
