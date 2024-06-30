def f1(self,x,y):
    return min(x,y)
class C:
    f=f1
    def g(self):
        print("hello world")
C1=C
print(C1.f(10,20))
C1.g()
    
    