class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')



# 학생을 표현하기 위한 클래스 생성
class Student(Person) :
    def __init__ (self, name, age, gpa):
        self.name=name
        self.age=age
        self.gpa=gpa

    def study(self):
        self.gpa += 0.1

# 교수 표현하기 위한 클래스 생성
class Professor(Person):
    def __init__(self, name, age, department):
        self.name=name
        self.age=age
        self.department=department

    def teach(self):
        self.age += 1

p1 = Professor('박교수', 49, '컴공')
s1 = Student('김학생',20, 3.5)

p1.talk()
s1.talk()


