#ass1:wap to print how many vowel there in the given string
s=input()
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c=c+1
print(c)