#hacker rank diagonal difference problem
n=int(input())
mat=[]
for i in range(0,n):
        l=list(map(int,input().split()))
        mat.append(l)
pd=0
sd=0
for i in range(0,n):
        for j in range(0,n):
                if i==j:
                        pd=pd+mat[i][j]
                if i+j==n-1:
                        sd=sd+mat[i][j]
    
    
print(abs(pd-sd))