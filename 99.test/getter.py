class Person:
    def __init__(self):
        self._age = 0


    @property
    def age(self):      # getter
        print('getter 호출 !')
        return self._age

    @age.setter
    def age(self, age):     # setter
        print('setter 호출 !')
        self._age = age

    # age = property(get_age,set_age)

p1 = Person()
# p1._age = 25 # 이거 안됨

# print(p1._age) # 이거 안됨

p1.age=25
print(p1.age)