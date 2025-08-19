def dect(func):
    def wrapper():
        print("This is starting")
        func()
        print("This is ending")
    return wrapper
@dect
def funcs():
    print("This is a function")
@dect
def sum():
    print(10+10)
funcs()
sum()