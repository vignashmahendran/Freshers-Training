import pandas as pd
import os
print("Combine Two CSV to Single File")
csv_file1=input("Enter csv file 1 : ")
csv_file2=input("Enter csv file 2 :  ")
csv_merge_file=input("Enter csv file to store merged csv:  ")
try:
    df1=pd.read_csv(csv_file1)
    df2=pd.read_csv(csv_file2)
    common_col=list(set(df1) & set(df2))
    common_col[0]
    output=pd.merge(df1,df2,on=common_col,how="inner")
    output.to_csv(csv_merge_file)
    print("merged csv file at" + os.path.abspath(csv_merge_file))
except Exception as e:
    print(e)