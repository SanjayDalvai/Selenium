class father:
    def func1(self):
        print("This is father")


class mother(father):
    def func2(self):
        print("This is mother")


class child(mother):
    def func3(self):
        print("This is Child")


obj=child()
obj.func1()
obj.func2()
obj.func3()