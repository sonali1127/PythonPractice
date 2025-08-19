'''Ass2:
Write a program to generate students results(sno,sname, group,S1,S2,S3)
Calculate total and avg.
If avg>=90,O-Grade
If avg>=80,A-Grade
If avg>=70,B-Grade
If avg>=60,C-Grade
If avg>=50,D-Grade
Otherwise Print Pass'''
sno=int(input("enter sno:"))
sname=input("enter sname:")
group=input("enter group:")
s1=int(input("enter s1:"))
s2=int(input("enter s2:"))
s3=int(input("enter s3:"))
tot=s1+s2+s3
avg=tot//3
if avg>=90:
    print("O-Grade")
elif avg>=80:
    print("A-Grade")
elif avg>=70:
    print("B-Grade")
elif avg>=60:
    print("C-Grade")
elif avg>=50:
    print("D-Grade")
else:
    print("Pass")