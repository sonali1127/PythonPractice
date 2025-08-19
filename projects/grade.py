from tkinter import *
def grading():
    g1=int(sem1a.get())
    g2=int(sem2a.get())
    g3=int(sem3a.get())
    g4=int(sem4a.get())
    g5=int(sem5a.get())
    g6=int(sem6a.get())
    tot=g1+g2+g3+g4+g5+g6
    avg=round((tot/6),2)
    if avg>=10:
        gr='0'
    elif avg>=9:
        gr='A+'
    elif avg>=8:
        gr='A'
    elif avg>=7:
        gr='B'
    elif avg>=6:
        gr='C'
    elif avg>=5:
        gr='D'
    elif avg>=4:
        gr='P'
    else:
        gr='F'  
    gpa='CGPA : '+str(avg)+"Result : "+gr
    bgpa.config(text=gpa)  
grade=Tk()
grade.title("Overall Grade")
sem1=Label(grade,text='SEM 1:')
sem1a=Entry(grade)
sem1.grid(row=0,column=0)
sem1a.grid(row=0,column=1)
sem2=Label(grade,text='SEM 2:')
sem2a=Entry(grade)
sem2.grid(row=1,column=0)
sem2a.grid(row=1,column=1)
sem3=Label(grade,text='SEM 3:')
sem3a=Entry(grade)
sem3.grid(row=2,column=0)
sem3a.grid(row=2,column=1)
sem4=Label(grade,text='SEM 4:')
sem4a=Entry(grade)
sem4.grid(row=3,column=0)
sem4a.grid(row=3,column=1)
sem5=Label(grade,text='SEM 5:')
sem5a=Entry(grade)
sem5.grid(row=4,column=0)
sem5a.grid(row=4,column=1)
sem6=Label(grade,text='SEM 6:')
sem6a=Entry(grade)
sem6.grid(row=5,column=0)
sem6a.grid(row=5,column=1)
res=Button(grade,text='Result',command=grading)
res.grid(row=6,column=0)
bgpa=Label(grade,text="?")
bgpa.grid(row=6,column=1)
grade.mainloop()

