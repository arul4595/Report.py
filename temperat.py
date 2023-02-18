import os,sys,socket,queue,datetime,time,threading,requests,json,schedule,copy,psutil
from openpyxl import Workbook,load_workbook
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

setting_file = open('cam.txt', 'r')
print("MT: I am a Server")
summary_dic = {"A": 'summary_a_list', "B": 'summary_b_list', "C": 'summary_c_list'}

filedic = {}
for line in setting_file:
    file_data = line.strip().split('===')
    #print(file_data)
    a = file_data[0]
    #print(a)
    b = file_data[1]
    #print(b)
    filedic[a] = b
    #print(filedic)
setting_file.close()

breadth = filedic.pop('breadth')

width=int(filedic.pop('width'))
print(filedic)
x ={ 'name':"John",
     "age":30,
     "city":"New York"}
a=[13,'arul', 'kumaran', False]

# parse x:
y = json.dumps(x)



employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#with open('example.txt', 'w') as exm:
 #   json.dump(x, exm, indent=2)
pers= open('example.json', 'w')
json.dumps(x, pers, indent=3, sort_keys=True)


print(json.dumps(x, indent=1))
print(json.dumps(x, indent=1, separators=(", ", " = ")))

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()


