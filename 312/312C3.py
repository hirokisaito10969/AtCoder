def count_sellers(ripeness, apples):
    # 二分探索を利用してりんごを売る価格 ripeness 以下の売り手の数を求める
    left, right = 0, len(apples)
    while left < right:
        mid = (left + right) // 2
        if apples[mid] <= ripeness:
            left = mid + 1
        else:
            right = mid
    return left

def count_buyers(ripeness, apples):
    # 二分探索を利用してりんごを買う価格 ripeness 以上の買い手の数を求める
    left, right = 0, len(apples)
    while left < right:
        mid = (left + right) // 2
        if apples[mid] >= ripeness:
            right = mid
        else:
            left = mid + 1
    return len(apples) - left

def find_minimum_price(N, M, seller_prices, buyer_prices):
    # 価格の昇順にソート
    seller_prices.sort()
    buyer_prices.sort()

    left, right = seller_prices[0], buyer_prices[-1]
    
    while left < right:
        mid = (left + right) // 2
        num_sellers = count_sellers(mid, seller_prices)
        num_buyers = count_buyers(mid, buyer_prices)
        if num_sellers >= num_buyers:
            right = mid
        else:
            left = mid + 1
    return left

# 入力を受け取る
N, M = map(int, input().split())
seller_prices = list(map(int, input().split()))
buyer_prices = list(map(int, input().split()))

# 最小の価格を求める
result = find_minimum_price(N, M, seller_prices, buyer_prices)
print(result)

# 5 WA