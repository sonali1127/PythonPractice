class Person:
    name="sonu"
    @property
    def namin(self):
        return self.name
    @namin.setter
    def naming(self,val):
        self.name=val
a=Person()
print(a.name)
a.naming="sona"
print(a.name)