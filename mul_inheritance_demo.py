class A:
    def __init__(self,a):
        self.a=a

    def process(self):
        print("A")

class B:
    def __init__(self,b):
        self.b=b

    def process(self):
        print("B")

class C(B,A):
    def __init__(self,a,b,c):
        B.__init__(self,b)
        A.__init__(self,a)
        self.c=c

    def process(self):
        print("C")

obj= C(1,2,3)
obj.process()
# Method Resloution Order
print(C.mro())


