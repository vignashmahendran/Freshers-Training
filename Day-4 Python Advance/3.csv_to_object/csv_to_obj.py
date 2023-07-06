import csv
import json
employee_list=[]
keys=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY','COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID']
with open("./Data_set/test.csv",'r') as data:
    dict_1=csv.DictReader(data)

    employee_list=list(dict_1)



class Employee:
    def __init__(self,dict1):
        self.EMPLOYEE_ID=dict1['EMPLOYEE_ID']
        self.FIRST_NAME=dict1['FIRST_NAME']
        self.LAST_NAME=dict1['LAST_NAME']
        self.EMAIL=dict1['EMAIL']
        self.PHONE_NUMBER=dict1['PHONE_NUMBER']
        self.HIRE_DATE=dict1['HIRE_DATE']
        self.JOB_ID=dict1['JOB_ID']
        self.SALARY=dict1['SALARY']
        self.COMMISSION_PCT=dict1['COMMISSION_PCT']
        self.MANAGER_ID=dict1['MANAGER_ID']
        self.DEPARTMENT_ID=dict1['DEPARTMENT_ID']
        
         
            
result_object=[]

for e in employee_list:
    result_object.append(Employee(e))


search=int(input("Enter Employee id to search  :  ")       )
print(result_object[search])
print('EMPLOYEE_ID  ',result_object[search].EMPLOYEE_ID)
print('FIRST_NAME  ',result_object[search].FIRST_NAME)
print('LAST_NAME ',result_object[search].LAST_NAME)
print('EMAIL ',result_object[search].EMAIL)
print('PHONE_NUMBER ',result_object[search].PHONE_NUMBER)
