
# x='글로벌!'
my_list = [1,2,3,4]

def func1():
    my_list[1] = 5554
    pass
    # global x # 안쪽은 글로벌 친구 가져오는 것? 
    # x= '인클로징!'
    # print(x)

    # def func2(a,b):
    #     x = '로컬!'
    #     print(x)
        # print(locals()) # 로컬에 위치한 변수 볼 수 있음
        # print(globals())
    
    # func2(2,3)

func1()
# print(x)
print(my_list)
