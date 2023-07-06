import os
import pandas as pd



print("----------Data Analysis in Employee Dataset --------")

#Data frame convertion

df=pd.read_csv('./Data_set/test.csv')

#Data Analysis in Employee Data set 

#Employee count
print('Number of Employee : '+str(df['EMPLOYEE_ID'].count()))

#Employee Salary  analysis

print("-------------Employee Salary  analysis-----------")
print("Employee Minimum salary : "+str(df['SALARY'].min()))
print("Employee Average salary  : "+str(df['SALARY'].mean()))
print("Employee Maximam salary : "+str(df['SALARY'].max()))
print("Total Expenture for Employee Salary : "+ str(df['SALARY'].sum()))

#Employee Department Analysis
print(" -----Depatment and its Employee count----- ")
print(df.groupby('JOB_ID').count()[['EMPLOYEE_ID','MANAGER_ID']])
print(df['DEPARTMENT_ID'].unique())

#Filter in Row and Column
print("------Employee with salary range in 2100 to 10000------")
print(df[(df.SALARY> 2100) &(df.SALARY< 10000)]['FIRST_NAME'])
print("-----record with empty last name------")
print(df[df.LAST_NAME.isnull()])

print("----Filter Email with regex ----")
print(df[df.EMAIL.str.contains("@email.com")])

