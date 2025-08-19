class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(self.id,self.name)
class Programmer(Employee):
    def lan(self):
        print("i am child")
e=Employee("Sonu",1200 )
e2=Programmer("Sona",1900)
e.show()
e2.show()
e2.lan()