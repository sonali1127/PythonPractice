'''assignment-2:
    write a program to prepare shopping mall bill
    pc=dussehra-50,weekend-40'''
shirt=1000
frock=500
sarees=2000
tshirt=500
shoes=600
print("**Welcome to Sirius Shopping Mall***")
cname=input('enter customer name:')
cphno=input('enter customer phone no:')
shirtq=int(input('Enter no of shirts:'))
frockq=int(input('Enter no of frocks:'))
sareesq=int(input('Enter no of sarees:'))
tshirtq=int(input('Enter no of tshirt:'))
shoesq=int(input('Enter no of shoes:'))
pc=input("enter promocode")
tot=(shirtq*shirt)+(frockq*frock)+(sareesq*sarees)+(tshirtq*tshirt)+(shoes*shoesq)
if pc=='dussehra' or pc=='DUSSHERA':
    disc=tot*50/100
elif pc=='weekend' or pc=='WEEKEND':
    disc=tot*40/100
elif tot>=5000:
    disc=tot*35/100
elif tot>=2000:
    disc=tot*25/100
elif tot>=1000:
    disc=tot*15/100
else:
    disc=tot*5/100
price=tot-disc
gst=price*18/100
amount=price+gst
print('***************')
print('custno:',cphno)
print('cutname:',cname)
print('bill:',tot)
print('Discount:',disc)
print('GST:',gst)
print('bill to be paid',amount)
print('Thank you!Visit Again')