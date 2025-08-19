''' write a program to calculate emi
where emi=si+principle_amount/no of months
where si=p*t*r/100 '''
p=int(input("enter principle amount:"))    
t=int(input("enter time:"))
r=eval(input("enter rate of interest:"))
si=(p*t*r)/100
emi=si+p/(12*t)
print(emi)