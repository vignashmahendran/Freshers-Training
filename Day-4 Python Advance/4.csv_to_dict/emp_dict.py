import csv
import json
employee_list=[]
keys=['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER','HIRE_DATE','JOB_ID','SALARY','COMMISSION_PCT','MANAGER_ID','DEPARTMENT_ID']
with open("./Data_set/test.csv",'r') as data:
    dict_1=csv.DictReader(data)

    employee_list=list(dict_1)

search=int(input("Enter Employee id to search  :  "))-1
emp_detail=employee_list[search]
for i in emp_detail:
    print(i +" : "+ emp_detail [i])


