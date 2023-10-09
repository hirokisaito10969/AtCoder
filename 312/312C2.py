def count_sellers(ripeness, apples):
    left, right = 0, len(apples)
    while left < right:
        mid = (left + right) // 2
        if apples[mid] <= ripeness:
            left = mid + 1
        else:
            right = mid
    return left

def count_buyers(ripeness, apples):
    left, right = 0, len(apples)
    while left < right:
        mid = (left + right) // 2
        if apples[mid] >= ripeness:
            right = mid
        else:
            left = mid + 1
    return len(apples) - left

def find_minimum_price(N, M, seller_prices, buyer_prices):
    seller_prices.sort()
    buyer_prices.sort()

    left, right = seller_prices[0], buyer_prices[-1]

    # 買い手の最安値が売り手の最高値を上回る場合
    if left > right:
        return buyer_prices[-1] + 1

    while left < right:
        mid = (left + right) // 2
        num_sellers = count_sellers(mid, seller_prices)
        num_buyers = count_buyers(mid, buyer_prices)
        if num_sellers >= num_buyers:
            right = mid
        else:
            left = mid + 1

    # 条件を満たす最小価格Xを求めるために、りんごをX円で売る売り手の人数を数える
    num_sellers = count_sellers(left, seller_prices)
    num_buyers = count_buyers(left, buyer_prices)
    while num_sellers >= num_buyers:
        left -= 1
        num_sellers = count_sellers(left, seller_prices)
        num_buyers = count_buyers(left, buyer_prices)

    return left + 1

# 入力を受け取る
N, M = map(int, input().split())
seller_prices = list(map(int, input().split()))
buyer_prices = list(map(int, input().split()))

# 最小の価格を求める
result = find_minimum_price(N, M, seller_prices, buyer_prices)
print(result)

# AC