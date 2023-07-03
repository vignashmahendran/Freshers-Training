import os

file_name=input("Please Enter File name with path :  ")
print('Enter "end" to terminate: ')
print("Please Enter Text To be save in a File :  ")

try:
    while(True):
        text=input()
        if(text.lower()=='end'):
            break
        file=open(file_name,'a')
        file.write(text+'\n')
        file.close()
        
    print("File Created Successfully at "+ os.path.abspath(file_name))

except Exception as e:
    print("There is a Problem in Writing File"+str(e))
    