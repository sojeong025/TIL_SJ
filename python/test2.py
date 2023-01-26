# 문자열이 주어지면 숫자, 문자, 기호가 몇개인지 출력하는 함수를 만들어라.
 
def check(input_str):
    char_count =0
    digit_count=0
    symbol_count=0

    for char in input_str:
        if char.isalpha(): #문자열인지 확인하는 메소드
            char_count += 1

        elif char.isdigit(): #숫자인지 확인하는 메소드
            digit_count += 1
        else:
            symbol_count +=1

    return char_count, digit_count, symbol_count

input_str = "123#%$aiden_snow"
char_count,digit_count, symbol_count = check(input_str)
# print(f"char: {char_count}, digit: {digit_count}, symbol: {symbol_count}")



sample_list = [ 11, 22, 33, 55, 66]

# 주어진 리스트의 4번째(index 3번) 자리에 있는 항목을 제거하고 변수에 할당해주세요.
# print("original list: ", sample_list)
fourth=sample_list.pop(3)
# print("list list: ", sample_list)
# print("fourth: ",fourth)

# sample_list의 가장 뒤에 77를 추가해보세요.
sample_list.append(77)

# 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요. 
sample_list.insert(2, fourth)
# print(sample_list)


my_tuple = (11,22,33,44,55,66)

# 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요.
# new_tuple = my_tuple.index[3:5]
# print(new_tuple)


a=[1,2,3]
b=a[:]
# print(a,b) # [1,2,3] [1,2,3]
b[0]=5
# print(a,b) # [1,2,3] [5,2,3]

a=[1,2,['a','b']]
b=a[:]
# print(a,b) # [1,2,['a','b']] [1,2,['a','b']]
b[2][0] =0
# print(a,b) # [1,2,[0,'b']] [1,2,[0,'b']]

import copy
a=[1,2,['a','b']]
b=copy.deepcopy(a)
# print(a,b) # [1,2,['a','b']] [1,2,['a','b']]
b[2][0] =0
# print(a,b) # [1,2,['a','b']] [1,2,[0,'b']]

# 람다
test_list= [1,2,3,7,4,6,5]
test_list.sort()
# print(test_list)

scores= [('eng',88),('sci',90),('math',80)]

def check(x):
    return x[1]

# 정렬
print(scores)
scores.sort(key=lambda x: x[1])
print(scores)