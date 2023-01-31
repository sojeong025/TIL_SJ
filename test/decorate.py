def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print("^~^//")

    return wrapper


@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')




ko_hello('sojeong')
en_hello('sojeong')

class Myclass:
        def method(self):
            return 'instance method', self
        @classmethod
        def classmethod(cls):
            return 'class method', cls
        @staticmethod
        def staticmethod():
            return 'static method'

my_class=Myclass()
print(my_class.method())
print(my_class.classmethod())
print(my_class.staticmethod())
