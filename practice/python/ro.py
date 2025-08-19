def myresult():
    s1=int(engmarks.get())
    s2=int(telmarks.get())
    s3=int(mathsmarks.get())
    s4=int(phymarks.get())
    s5=int(csmarks.get())
    s6=int(projectmarks.get())
    total=s1+s2+s3+s4+s5+s6
    avg=total//6
    if avg>=90:
        gr="OutStanding"
        print("outstanding")
    elif avg>=70:
        gr="First"
    elif avg>=60:
        gr="Second"
    elif avg>=50:
        gr="Third"
    elif avg>=40:
        gr="Pass"
    else:
        gr="Fail"
    s="Total:"+str(total)+" Grade:"+gr
    res.config(text=s)



from tkinter import *
result=Tk()
result.title("Student Result")
eng=Label(result,text="Enter English Marks:")
engmarks=Entry(result)
tel=Label(result,text="Enter Telugu Marks:")
telmarks=Entry(result)
maths=Label(result,text="Enter Maths Marks:")
mathsmarks=Entry(result)
phy=Label(result,text="Enter Physics Marks:")
phymarks=Entry(result)
cs=Label(result,text="Enter Computer Marks:")
csmarks=Entry(result)
project=Label(result,text="Enter Project Marks:")
projectmarks=Entry(result)
b1=Button(result,text="Submit",command=myresult)
res=Label(result,text="?")
eng.grid(row=0,column=0)
engmarks.grid(row=0,column=1)

tel.grid(row=1,column=0)
telmarks.grid(row=1,column=1)

maths.grid(row=2,column=0)
mathsmarks.grid(row=2,column=1)

phy.grid(row=3,column=0)
phymarks.grid(row=3,column=1)

cs.grid(row=4,column=0)
csmarks.grid(row=4,column=1)

project.grid(row=5,column=0)
projectmarks.grid(row=5,column=1)

b1.grid(row=6,column=0)
res.grid(row=6,column=1)

result.mainloop()
    