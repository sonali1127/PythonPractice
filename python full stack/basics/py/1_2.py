import random
import string
def encode():
    words=input("Enter the string to Encode:").split(" ")
    word=[]
    for s in words:
        if len(s)>2:
            a="".join(random.choices(string.ascii_lowercase,k=3))
            b="".join(random.choices(string.ascii_lowercase,k=3))
            word.append(a+s[1:]+s[0]+b)
        else:
            word.append(s[::-1])
    print(" ".join(word))
def decode():
    words=input("Enter the string to Decode:").split()
    word=[]
    for s in words:
        if len(s)>2:
            word.append(s[-4]+s[3:len(s)-4])
        else:
            word.append(s[::-1])
    print(" ".join(word))

choice=int(input("Enter your choice to Encode press 1 and for Decode press 2:"))
if choice==1 or choice==2:
    if choice==1:
        encode()
    else:
        decode()
else:
    choice=int(input("Enter your choice to Encode press 1 and for Decode press 2:"))
