import pandas as pd

#File path
print('Employee and their average performance')
employee_csv=input("Enter employee detail csv file path :")
performance_csv=input("Enter employee performance csv file path :")
result_csv=input("output csv file with path")
#data frame operation on csv 
employee_df=pd.read_csv(employee_csv)
performance_df=pd.read_csv(performance_csv)

#listing common field
common_column=list(set(employee_df) & set(performance_df))
#merge data frames
merged_df=pd.merge(employee_df,performance_df,on=common_column,how="left")

result=merged_df.groupby(['Id',"Name","City"])['Performance'].mean()

result.to_csv(result_csv)
