import csv
import json
import os
input_csv_file=input("Enter csv file with path : ")
output_json_file=input("Enter JSON output file with path: ")
data_list=[]
try:
    with open(input_csv_file,'r') as csv_file:
        csv_read=csv.DictReader(csv_file)
        for rows in csv_read:
            data_list.append(rows)
    with open(output_json_file,'w') as json_file:
        json_file.write(json.dumps(data_list,indent=4))
        print("JSON file is created at "+os.path.abspath(output_json_file))

    

except Exception as e:
    print("Some Error has occured"+ str(e)) 