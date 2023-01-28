def winner_is(coins, n):
    matrix = [[0 for i in range(n)] for i in range(n)]
    for distance in range(n):
        for j in range(distance, n):
            i = j - distance
            x = 0
            if i + 2 <= j:
                x = matrix[i + 2][j]
            y = 0
            if i + 1 <= j - 1:
                y = matrix[i + 1][j - 1]
            z = 0
            if i <= j - 2:
                z = matrix[i][j - 2]
            matrix[i][j] = max(coins[i] + min(x, y), coins[j] + min(y, z))
    return matrix[0][n - 1]
 
 
n = int(input())
coins = list(map(int, input().split()))
result = winner_is(coins, n)

if result > (sum(coins) - result):
    print(f'Победил 1-й игрок, сумма выигрыша: {result}')
elif result < (sum(coins) - result):
    print(f'Победил 2-й игрок, сумма выигрыша: {result}')
else:
    print(f'Ничья: игроки выиграли по {result}')
