def find_missing_number(N, nums):
    min_num = min(nums)
    max_num = max(nums)
    
    total_expected_sum = (min_num + max_num) * (N + 1) // 2
    actual_sum = sum(nums)
    
    missing_number = total_expected_sum - actual_sum
    return missing_number

N = int(input())
nums = list(map(int, input().split()))

missing_number = find_missing_number(N, nums)
print(missing_number)
