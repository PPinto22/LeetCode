def solve(test_case, budget, prices):
    spent = 0
    houses = 0
    for price in sorted(prices):
        if spent + price > budget:
            break
        spent += price
        houses += 1
    print('Case #{}: {}'.format(test_case, houses), flush=True)


t = int(input())
for x in range(1, t+1):
    n, b = map(int, input().split())
    prices = map(int, input().split())
    solve(x, b, prices)