class parent:
    def func1(self):
        print("this is function 1")
class child(parent):
    def func2(self):
        print("this is function 2")
class child2(child):
    def func3(self):
        print("this is function 3")
ob=child2()
ob.func1()
ob.func2()
