if __name__ == '__main__':
    N = int(input())
    l=[]
    for j in range(1,N+1):
        p=input().split()
        if p[0]=='insert':
            i=int(p[1])
            e=int(p[2])
            l.insert(i,e)
        elif p[0]=='print':
            print(l)
        elif p[0]=='remove':
            x=int(p[1])
            l.remove(x)
        elif p[0]=='append':
            x=int(p[1])
            l.append(x)
        elif p[0]=='sort':
            l.sort()
        elif p[0]=='pop':
            l.pop()
        elif p[0]=='reverse':
            l.reverse()
