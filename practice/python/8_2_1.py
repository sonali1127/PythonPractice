#ass1:create student dictionary with 5 subjects and generate results
d={}
n=int(input("Enter no of students:"))
for i in range(n):
    l=[]
    htno=int(input("Enter hall ticket no:"))
    sname=input("enter name:")
    s1=int(input("enter s1:"))
    s2=int(input("enter s2:"))
    s3=int(input("enter s3:"))
    s4=int(input("enter s4:"))
    s5=int(input("enter s5:"))
    l.append(sname)
    l.append(s1)
    l.append(s2)
    l.append(s3)
    l.append(s4)
    l.append(s5)
    d[htno]=l
hno=int(input("enter hall ticket:"))
print("Name:",d[hno][0])
total=sum(d[hno][1:])#d[hno][1]+d[hno][2]+d[hno][3]+d[hno][4]+d[hno][5]
avg=total//5
print("Total:",total)
print("Percentage:",avg)
if avg>60:
    print("pass")
else:
    print("fail")