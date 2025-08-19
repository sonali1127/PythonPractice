'''write a program to read sno,sname,group,3 subjects
    and print total and avg
ex:sno=1,name=sai,group=mpcs,s1=80,s2=70,s3=60
output:total:210,avg-70'''
sno=int(input("enter sno:"))
sname=input("enter sname:")
group=input("enter group:")
s1=int(input("enter s1:"))
s2=int(input("enter s2:"))
s3=int(input("enter s3:"))
tot=s1+s2+s3
print("total:",tot)
print("avg:",tot/3)