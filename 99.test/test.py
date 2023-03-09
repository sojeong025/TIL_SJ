def func1():
    print('func1 시이작')

    def func2():
        print('func2 시이작')
        print('func2 끄읕')
        return

    func2()
    return

func1()