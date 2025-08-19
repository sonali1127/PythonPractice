'''assignment-1:
    write a program to print given year is leap year or not'''
year=int(input("enter the year:"))
if(year%4==0 and year%100!=0)or year%400==0:
    print(year,"is leap year")
else:
    print(year,"is not a leap year")