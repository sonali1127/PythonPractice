'''write a program to check the whether student is pass or fail sno,sname,group,s1,s2,s3 pass constraint,marks should greater than or equal to 40,
if the condition is true,then print pass otherwise print fail
s1>=40 s2>=40 s3>=40 '''
sno=int(input("enter sno:"))
sname=input("enter sname:")
group=input("enter group:")
s1=int(input("enter s1:"))
s2=int(input("enter s2:"))
s3=int(input("enter s3:"))
if(s1>=40 and s2>=40 and s3>=40):
    print("Pass")
else:
    print("Fail")



