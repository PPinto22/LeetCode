def solve(u, queries):
    alphabet = get_alphabet(queries)
    # (letter, count) sorted by count DESC
    counts = count_most_significant_digits(queries)

    key = []
    for i in range(10):
        # 0 is the one that never appears as the first digit
        if i == 0:
            letter = [letter1 for letter1 in alphabet if letter1 not in
                      [letter2 for (letter2, count) in counts]][0]
        else:
            letter = counts[i-1][0]
        key.append(letter)
    return ''.join(key)


def get_alphabet(queries):
    found = 0
    alphabet = set()
    for (q, r) in queries:
        for c in r:
            alphabet.add(c)
        if len(alphabet) == 10:
            break
    return alphabet


def count_most_significant_digits(queries):
    counts = {}
    for (q, r) in queries:
        digit = r[0]
        if digit not in counts:
            counts[digit] = 0
        counts[digit] += 1
    return [(letter, count) for (letter, count) in
            sorted(counts.items(), key=lambda item: item[1], reverse=True)]

if __name__ == '__main__':
    T = int(input())
    for Ti in range(1, T + 1):
        u = int(input())
        queries = []
        for _ in range(10 ** 4):
            # q is -1 if unknown
            line = input().split()
            q, r = int(line[0]), line[1]
            queries.append((q, r))
        result = solve(u, queries)
        print('Case #{}: {}'.format(Ti, result))
