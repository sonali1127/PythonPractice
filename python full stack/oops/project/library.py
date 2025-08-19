class Library:
    def __init__(self):
        self.noOfBooks=0
        self.books=[]
    def addBooks(self,book):
        self.books.append(book)
        self.noOfBooks+=1
    def noOfBooksCheck(self):
        if self.noOfBooks == len(self.books):
            print("Books are stored perfectly")
    def showDetails(self):
        print(f"This library has {self.noOfBooks}.")
        print("BOOKS")
        for i in self.books:
            print(i)
a=Library()
a.addBooks("Sonu")
a.addBooks("Sonu1")
a.addBooks("Sonu2")
a.addBooks("Sonu3")
a.showDetails()
a.noOfBooksCheck()