class A:
    def __init__(self,name):
        self.name=name
    def show(self):
        return f"Grandpa ,Your name is {self.name}"
class B(A):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        return f"{super().show()}\n Father ,name is {self.name}"
class C(B):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        return f"{super().show()}\n child2 ,name is {self.name}"
class D(B):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        return f"{super().show()}\n child1 ,name is {self.name}"
a=D("wase")
b=C("paise")
c=B("kaise")
d=A("raita")
print(a.show())
print()
print(b.show())
print()
print(c.show())
print()
print(d.show())
print()