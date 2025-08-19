#write a program to generate student results(First,Second,Third,Pass)
sno=int(input('Enter student no:'))
sname=input('Enter student name:')
group=input('Enter student group:')
s1=int(input('Enter Web programming:'))
s2=int(input('enter R language:'))
s3=int(input('enter Cyber law:'))
tot=s1+s2+s3
avg=tot//3
print('student name:',sname)
print("student no:",sno)
print("Student Group:",group)
print('total marks:',tot)
print('avg marks:',avg)
if avg>90:
    print("First Class")
elif avg>75:
    print("Second Class")
elif avg>60:
    print("Third Class")
elif avg>35:
    print("Pass")
else:
    print("Fail")