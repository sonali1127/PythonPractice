f1=open("myfile.txt","r")
f2=open("myfile.txt","w")
f3=open("myfile.txt","a")#to read/write/append binary line rb,wb,ab
t=f1.read()
t2=f2.write("some text")
t3=f3.write("appends text")
f1.close()
f2.close()
f3.close()
#with open("","") we do not need close 