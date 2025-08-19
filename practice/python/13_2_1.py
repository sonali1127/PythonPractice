'''#write a program to generate salary bill for employee
emno,empname,designation,basic,hra,da,ta
print empno,empname,designation,basic,hra,da,ta,netsalary,tax
where netsalary=basic+da+ta+hra
where tax is depending on net salary
if netsalary>50,000->tax is 5%
if netsalary>35000->tax is 3%
it netsalary>20000->tax is 1%
otherwise tax=0'''
class Salary:
    def getdata(self,empno,empname,des,basic,hra,da,ta):
        self.empno=empno
        self.empname=empname
        self.des=des
        self.basic=basic
        self.hra=hra
        self.da=da
        self.ta=ta
    def putdata(self):
        print("Employee No:",self.empno)
        print("Employee Name:",self.empname)
        print("Designation:",self.des)
        print("Basic Pay:",self.basic)
        print("H.R.A:",self.hra)
        print("D.A:",self.da)
        print("T.A:",self.ta)
        net=self.basic+self.da+self.ta+self.hra
        print("Net salary:",net)
        if net>50000:
            tax=(5/100)*net
        elif net>35000:
            tax=(3/100)*net
        elif net>20000:
            tax=(1/100)*net
        else:
            tax=0
        print("Tax:",tax)
ob=Salary()
empno=input("Enter employee no:")
empname=input("Enter employee name:")
des=input("Enter designation:")
basic=int(input("Enter basic pay:"))
hra=int(input("Enter hra:"))
da=int(input("Enter da:"))
ta=int(input("Enter ta:"))
ob.getdata(empno,empname,des,basic,hra,da,ta)
ob.putdata()


