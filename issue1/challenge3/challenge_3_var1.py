def winner_is(coins, n):
    memo_dict = {}
 
    def options(i, j):
        if i > j or i >= n or j < 0:
            return 0
 
        k = (i, j)
        if k in memo_dict:
            return memo_dict[k]
  
        opt1 = coins[i] + min(options(i + 2, j), options(i + 1, j - 1))
        opt2 = coins[j] + min(options(i + 1, j - 1), options(i, j - 2))
        memo_dict[k] = max(opt1, opt2)
        return memo_dict[k]
    return options(0, n - 1)
 
n = int(input())
coins = list(map(int, input().split()))
 
result = winner_is(coins, n)
if result > (sum(coins) - result):
    print(f'Победил 1-й игрок, сумма выигрыша: {result}')
elif result < (sum(coins) - result):
    print(f'Победил 2-й игрок, сумма выигрыша: {result}')
else:
    print(f'Ничья: игроки выиграли по {result}')
