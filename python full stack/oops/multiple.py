class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        return f"Your name is {self.name}"
class Mother:
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        return f" My name is {self.name}"
class Child(Father,Mother):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f"name is {self.name}"
a=Child("jaya")
print(a.show())