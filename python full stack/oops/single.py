class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        return f"The parent name and age is {self.name} and {self.age}"
class Child(Parent):
    def __init__(self,name,age,cls):
        super().__init__(name,age)
        self.cls=cls
    def __str__(self):
        return f"The child class is {self.cls}"
p=Parent("sda",12)
a= Child("sda",12,"5")
print(a,a.show())