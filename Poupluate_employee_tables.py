# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:58:40 2022

@author: PVS
"""

import random
from   datetime          import  datetime
import sys, os
import random
import string
import mysql.connector
# pip install mysql-connector-python 
folder_name = r'E:\DSE-MOCK-INTERVIEW'

sys.path.insert(0, folder_name) 

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

from db_Class_220621  import  Employee

error = None
emp              =    Employee("localhost","testUser", "A4min@123","hr" )
connection       =    emp.db_connection()
emp.db_create_table()
        
### 
### Insert data 
###
        
n =  20

EMPID_LIST     =     list()
        
for i in range(n):
        
            FN_list = ["Arun", "Arockia", "Alex", "Amin", "Bhim", "Chandar", "Durvan", "Durvik", "Dhanis", "Yashnav", \
                       "Sheshvan", "Sowgatha", "Vijaychandra", "Vijay", "Praveen", "Arya", "Ritesh", "Piyush",\
                       "Arya","Xavier"]
            
            FN_list_Female= ["Anika", "Parvathi Devi", "Aslesha", "Aashna", "Ahalya", "Anamika",\
                             "Bianca", "Binal", "Bina", "Bagya", "Saranya", "Diana", "Disha",\
                             "Deepti", "Esha", "Estaa", "Eshika", "Firaki", "Fanha", "Gina", "Gauri",\
                             "Hasina", "Hrithika", "Isha", "Iravati"]
            DEPTNAME_list =  ['HR & Admin', 'Finance & Accounts' , 'Production', 'Sales & Marketing', 'Purchase'] 
            
            DEPTNAME      =  random.choice(DEPTNAME_list)  
            DEPTNAME      =  random.choice(DEPTNAME_list)  
            DEPT_ID       =  str(DEPTNAME_list.index(DEPTNAME)  +  1) 

            DOJ_list      =  ['1990-01-31', '1998-10-31','1997-03-31','2000-04-01','2001-04-11',\
                              '1995-07-21', '2002-05-24','2004-01-22','2008-07-01','2010-08-01',\
                              '1997-11-01', '1997-11-01','1996-09-20','2014-02-03','1993-11-03',\
                              '2010-01-11', '2009-11-09','2017-10-20','2009-10-11','2008-03-20']    
          
            DOJ           =  random.choice(DOJ_list)
            
            EMP_ID        =  str(random.randrange(1000, 9000))    
            FN            =  random.choice(FN_list)
            LN            =  random.choice(random.choice(string.ascii_uppercase))
            AGE           =  str(random.choice(list(range(21, 66))))
            SEX           =  random.choice(['M', 'F'])
            INCOME        =  str(round(float(random.random()) * 100000,0))
           
            try:
                print(EMP_ID)
                EMPID_LIST += [EMP_ID]
            except:
                print('Error')
            
            emp.insertVariblesIntoTable(EMP_ID, DEPT_ID, FN, LN, AGE, 'M', INCOME, DOJ) # Male employees

            EMP_ID        =  str(random.randrange(100, 900))    
            FN_Female     =  random.choice(FN_list_Female)    
            LN            =  random.choice(random.choice(string.ascii_uppercase))
            AGE           =  str(random.choice(list(range(21, 65))))
            SEX           =  random.choice(['M', 'F'])
            INCOME        =  str(round(float(random.random()) * 100000,0))
            
            try: ## Error
                print(EMP_ID)
                EMPID_LIST += [EMP_ID]
            except:
                print('Error')
                        
            emp.insertVariblesIntoTable(EMP_ID, DEPT_ID, FN_Female, LN, AGE, 'F', INCOME, DOJ) # Female employees
            
            

###

DEPTNAME_list      =  ['HR & Admin', 'Finance & Accounts' , 'Production', 'Sales & Marketing', 'Purchase'] 
MANAGER_list       =  ['HR00', 'FA00' , 'PR00' , 'SM00', 'PU00']
NAME_list          =  ['Rosy' , 'Peter', 'Arul', 'Murugan', 'Sowmya']
LN                 =  random.choice(random.choice(string.ascii_uppercase))
SEX_list           =  ['F', 'M', 'M', 'M', 'F']
DOJ_list_Manager   =  ['2010-01-11', '2009-11-09','2017-10-20','2009-10-11','2008-03-20']  

for i in range(len(DEPTNAME_list)):
    DEPTNAME       =  DEPTNAME_list[i]  
    DEPT_ID        =  str(i +  1) 
    EMP_ID         =  MANAGER_list[i] 
    FN_MANAGER     =  NAME_list[i]
    LN             =  random.choice(random.choice(string.ascii_uppercase))
    SEX            =  SEX_list[i]
    DOJ            =  DOJ_list_Manager[i]
    
    emp.insertVariblesIntoTable(EMP_ID, DEPT_ID, FN_MANAGER, LN, AGE, SEX, INCOME, DOJ)  
    emp.insertVariblesIntoTable2(DEPT_ID, DEPTNAME, EMP_ID)

###
### Insert records into leaves table
### 

from datetime import datetime, timedelta


print(EMPID_LIST)   
       
for  i in range(5):
    
     EMP_ID      =   random.choice(EMPID_LIST)
     DATE_delt   =   random.randint(10, 365)
     start       =   datetime.now() + timedelta(days = -DATE_delt)
     start_date  =   start.strftime('%Y-%m-%d')
     LDAYS       =   random.randint(1, 10)
     end         =   start + timedelta(days= (LDAYS-1))
     end_date    =   end.strftime('%Y-%m-%d')    
     emp.insertVariblesIntoTable3(EMP_ID, start, end, str(LDAYS))

###

sql_select     =  """SELECT CONVERT(count(*), CHAR) FROM EMPLOYEE"""
cursor         =  connection.cursor()
cursor.execute(sql_select)
count          =  cursor.fetchone()
        
print("\n Total Employee records inserted is %s" % count)

sql_select1    =  """SELECT CONVERT(count(*), CHAR) FROM DEPARTMENT"""
cursor         =  connection.cursor()
cursor.execute(sql_select1)
count          =  cursor.fetchone()
        
print("\n Total Department records inserted is %s" % count)

sql_select     =  """SELECT CONVERT(count(*), CHAR) FROM LEAVES"""
cursor         =  connection.cursor()
cursor.execute(sql_select)
count          =  cursor.fetchone()
        
print("\n Total Leaves records inserted is %s" % count)

###