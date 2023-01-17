# 1~3의 세제곱 리스트 만들기
cubic_list=[]
for number in range(1,4):
    cubic_list.append(number ** 3)
print(cubic_list)

# [1, 8, 27]

cubic_list = [number ** 3 for number in range(1,4)]
print(cubic_list)

# [1, 8, 27]

# 1~3의 세제곱 딕셔너리 만들기
cubic_dict ={}

for number in range(1,4):
    cubic_dict[number] = number **3
print(cubic_dict)

# {1: 1, 2: 8, 3: 27}

cubic_dict={number: number ** 3 for number in range(1,4)}
print(cubic_dict)

# {1: 1, 2: 8, 3: 27}