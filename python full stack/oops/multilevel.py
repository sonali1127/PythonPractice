class A:
    def __init__(self,name):
        self.name=name
    def show(self):
        return f"Your name is {self.name}"
class B(A):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        return f"{super().show()} My name is {self.name}"
class C(B):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f"name is {self.name}"
a=C("jaya")
print(a.show())
ab=B("dev")
print(ab.show())