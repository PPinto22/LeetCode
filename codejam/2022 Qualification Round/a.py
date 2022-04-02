def print_punch_card(rows, columns):
    print('..+' + '-+' * (columns - 1))
    print('..|' + '.|' * (columns - 1))
    print('+-+' + '-+' * (columns - 1))

    for _ in range(rows - 1):
        print('|.|' + '.|' * (columns - 1))
        print('+-+' + '-+' * (columns - 1))


def main():
    n_test_cases = int(input())
    for case_i in range(1, n_test_cases + 1):
        rows, columns = map(int, input().split())
        print(f'Case #{case_i}:')
        print_punch_card(rows, columns)


if __name__ == '__main__':
    main()
