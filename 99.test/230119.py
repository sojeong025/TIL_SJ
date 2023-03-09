def my_magic_func(n):
    return n * 10

my_list = [1,2,3,4,5]

map_obj= map(my_magic_func, my_list)
print(list(map_obj))

# filter
def odd(n):
    return n%2
numbers = [1,2,3]
result = filter(odd,numbers)
print(result, type(result))
print(list(result))

# zip
name_list=['신동민','서재현','박영서','이태성','정예원','이은석']
age_list=[17,18,22,24,25,19]

for each in zip(name_list,age_list):
    print(each)

# lambda
# 삼각형의 넓이를 구하는 공식 -def
def triangle_area(b,h):
    return 0.5 * b * h
print(triangle_area(5,6))

# 삼각형의 넓이를 구하는 공식 - lambda
# lambda 매개변수 : 매개변수를 이용한 리턴값
triangle_area=lambda b,h : 0.5*b*h
print(triangle_area(5,6))

# 재귀함수 - 자기 자신을 호출하는 함수 -> 그림을 그려보기
def fac(n) :
    if n == 0 or n==1:
        return 1
    else:
        return n* fac(n-1)
print(fac(5))