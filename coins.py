def make_change(coins_values, change, min_coins, coins_used):
    for cents in range(change + 1):
        coins_count = cents
        new_coin = 1

        for j in [c for c in coins_values if c <= cents]:
            if min_coins[cents-j] + 1 < coins_count:
                coins_count = min_coins[cents - j] + 1
                new_coin = j

        min_coins[cents] = coins_count
        coins_used[cents] = new_coin

    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin -= this_coin


def main():
    amnt = 33
    clist = [1, 5, 8, 10, 25]
    coins_used = [0]*(amnt + 1)
    coins_count = [0]*(amnt + 1)

    print("Making change for", amnt, "requires")
    print(make_change(clist, amnt, coins_count, coins_used), "coins")
    print("They are:")
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)


main()