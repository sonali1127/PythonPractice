n=4
for i in range(n):
    for j in range(n):
        if i==j or j==n-1-i:
            print(i, end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    #world