import mysql.connector

conn = mysql.connector.connect(
host = "localhost",
user = "root",
passwd="root",
database='company'
)

mycursor = conn.cursor()

mycursor.execute('select * from employee')
for row in mycursor:
    print(row)
print('---------------------------------------------------------')
a=int(input('''
Enter 1 to Add Employee
Enter 2 to Remove Employee
Enter 3 to Search by name Employee
Enter 4 to Edit for Employee : '''))

if a == 1:
         for _ in iter(int,1):
               eid=int(input("Enter id employee : "))
               ename=input("Enter name employee : ")
               elast=input("Enter last name employee : ")
               esalary=int(input("Enter salary employee : "))
               edept=input("Enter department employee : ")
               print('-----------------------------------')
               s ='insert into employee values(%s,%s,%s,%s,%s)'
               inp=(eid,ename,elast,esalary,edept)
               mycursor.execute(s,inp)
               conn.commit()
elif a == 2:
               id=int(input("Enter id to remove by ID : "))
               print('-----------------------------------')
               mycursor.execute('delete from employee where empid = %d'%(id))
               conn.commit()
elif a == 3:
                sname=input('Enter name to search : ')
                sql='select * from employee where name = %s'
                data=(sname,)
                mycursor.execute(sql,data)
                result = mycursor.fetchone()
                print(result)
elif a == 4:
              # sname=input('Enter name to update : ')
               print('-----------------------------------')
               
               eid=int(input("Enter new id employee : "))
               ename=input("Enter new name employee : ")
               elast=input("Enter new last name employee : ")
               esalary=int(input("Enter new salary employee : "))
               edept=input("Enter new department employee : ")
               print('-----------------------------------')
               
               sql="update employee set empid=%d , name=%s , lastname=%s , salary=%d , dep=%s where empid=2"
               data=(eid,ename,elast,esalary,edept,)
               
               mycursor.execute(sql,data)
               conn.commit()




               

