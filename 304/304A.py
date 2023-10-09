N = int(input())
people = []

list2=[]
name1=[]
for _ in range(N):
    name, age = input().split()
    age = int(age)
    list2.append(age)
    name1.append(name)
    # people.append((name, age))

# people.sort(key=lambda x: x[1])  # 年齢で昇順ソート

min1 = min(list2)

start_index = list2.index(min1)

# start_index = 0


list1 = []
for i in range(N):
    list1.append(name1[start_index])
    start_index = (start_index + 1) % N  # 次の人のインデックスを計算して更新

for i in range(len(list1)):
    print(list1[i])