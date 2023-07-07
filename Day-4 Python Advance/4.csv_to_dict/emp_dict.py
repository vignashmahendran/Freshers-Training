import csv
employee_list={}
with open("./Data_set/test.csv",'r') as data:
    dict_1=csv.DictReader(data)
    for row in dict_1:
            employee_list[row['EMPLOYEE_ID']]=row
    
search=input("Enter Employee id to search  :  ")
emp_detail=employee_list[search]
for i in emp_detail:
    print(i +" : "+ emp_detail [i])


