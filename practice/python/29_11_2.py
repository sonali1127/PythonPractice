password=input("enter password:")
u=0
l=0
d=0
s=0
sp='@_$'
n=len(password)
for i in password:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
    elif i in sp:
        s=s+1
if n>=8 and u>0 and l>0 and d>0 and s>0:
    print("strong password")
elif u>0 and l>0 and s>0 and n>=8:
    print("medium password") 
elif u>0 or l>0 and n>=8:
    print("weak password")    
else:
    print("invalid")