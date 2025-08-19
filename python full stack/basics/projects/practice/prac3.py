def encryption(s):
    c=0
    while True:
        if "<>" in s:
            c=c+1
            s.replace(" ","<>")
        if "><" in s:
            c=c+1
            s.replace("><"," ")
        if not s:
            return c
    
    
s=input()
print(encryption(s))
