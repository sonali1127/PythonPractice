n=int(input())
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
for i in range(n):
    if l[i] > 0:
        print(1,end=" ")
    elif l[i] == 0:
        print("error") 
    else:
        print(l[i],end=" ")
