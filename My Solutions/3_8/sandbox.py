class Parent:
    def spam(self):
        print('Parent')

class A(Parent):
    def spam(self):
        print('A')
        super().spam()

class B(Parent):
    def spam(self):
        print('B')
        print(self)
        super().spam()

class C(A, B):
    def spam(self):
        print('C')
        super().spam()

class D(B):
    def spam(self):
        print('D')
        super().spam()

class Child(C, D):
    pass

c = Child()
c.spam()
print(Child.__mro__)
# Super returns the object of a class that is next on MRE