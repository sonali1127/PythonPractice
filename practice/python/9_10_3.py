# write a program to swapping of two numbers without using third variable
a=int(input("enter a value: "))
b=int(input("enter b value: "))
a=a+b;
b=a-b;
a=a-b;
print("a:",a)
print("b:",b)
# write a program to swapping of two numbers with using third variable
a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=a
a=b
b=c
print("a:",a)
print("b:",b)