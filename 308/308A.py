def check_sequence(nums):
    # 条件1の判定
    if not all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        return "No"

    # 条件2の判定
    if not all(100 <= num <= 675 for num in nums):
        return "No"

    # 条件3の判定
    if not all(num % 25 == 0 for num in nums):
        return "No"

    return "Yes"


# 入力を受け取る
inputs = input().split()

# 文字列から整数リストに変換
nums = [int(num) for num in inputs]

# 判定結果を出力
print(check_sequence(nums))
