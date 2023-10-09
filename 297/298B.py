# import re

# S = input()
# check1 = re.match(".*B(..)*B.*", S) is not None
# check2 = re.match(".*R.*K.*R.*", S) is not None

# if check1 and check2:
#     print("Yes")
# else:
#     print("No")

S = input()
c1 = (S.rfind('B') - S.find('B')) % 2 == 1
c2 = S.find('R') < S.find('K') < S.rfind('R')
print('Yes' if c1 and c2 else 'No')
