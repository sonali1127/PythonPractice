class Parent:
    def __init__(self,name):
        self.name=name
    def show(self):
        return f"Your name is {self.name}"
class Child1(Parent):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        return f"{super().show()} My name is {self.name}"
class Child2(Parent):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f"name is {self.name}"
a=Child1("jaya")
print(a.show())
ab=Child2("dev")
print(ab.show())