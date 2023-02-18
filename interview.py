A=5
b=2
print(A/b)
print(A//b)
print(A % b)

#polymorphism
class Pycharm:
    def execute(self):
        print('Compile')
        print('Run')


class Myeditor:
    def execute(self):
        print('Edit')
        print('Erase')
        print('Run')

class Laptop:
    def code(self, new):
        new.execute()

new = Pycharm()

lap1 = Laptop()
lap1.code(new)



#instance, class and staic variable
class Vehicle:
    Model = 'Nissan'

    def __init__(self, c1, v1, j1):
        self.car = c1
        self.van = v1
        self.jeep = j1

    def price_car(self):
        return 10000

    @classmethod
    def model_name(cls):
        return cls.Model

    @staticmethod
    def info():
        print('This is ex of vehicle')

Veh1 = Vehicle('car', 'van', 'jeep')
Veh2 = Vehicle('car1', 'van1', 'jeep1')
print(Veh1.price_car())
print(Vehicle.model_name())
Veh2.info()

#Single inheritance ans init method
class Person:
    def __init__(self, name, age):
        print('Im base')
        self.name = name
        self.age = age
    def display(self):
        print('Name is', self.name)
        print('Age is', self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, per):
        print('Welcome')
        self.rollno = roll_no
        self.percentage = per
        Person.__init__(self, name, age)
    def display(self):
        print("Roll no", self.rollno)
        Person.display(self)
        print('Percentile', self.percentage)

s1 = Student('Arul', 30, 40, 75.5)
# s2 = Person('Saru', 6)
s1.display()
# s2.display()



#Reverse print
print('arulkumaran'[1:5:1])
a='Welcome'
print(a[::-1])

#lambda function
func = lambda a, b : (a ** b)
print(func((10), 20))

# Connection of MSSQL Server
import pyodbc

conn = pyodbc.connect("Driver = SQL Server;"
                      "Server = WINS-GHJ/SPR4;"
                      "Database = SPR4;"
                      "Trusted_Connection = Yes")
cursor = conn.cursor()
sqlquery = f''' '''
cursor.execute(sqlquery)

# Connection of PLC
import snap7
from snap7 import util

client = snap7.client.Client()
client.connect('192.168.0.200', 0, 0)

client.get_connected()
db = client.db_read(5, 0, 5)
t = client.get_r

db = client.db_write(5, 0, 18)

# Difference lists and tuple
a=[10, 20, 3, 40]
b=(12, 3, 4, 1)
a[0]= 'arul'
print(a[0].split())
a.append(5)

#Enumerate function
sum1=0
for i, j in enumerate(a):
    sum1 += j
    print("st", i, sum1)
print(sum1)

#find out factorial
num1 = int(input("Enter the number "))
fact = 1
while num1 > 0:
    fact *= num1
    num1 -= 1
print(fact)