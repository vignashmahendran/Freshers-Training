import os
input_path=input("Enter Path of the Folder:  ")
output_path=input("Enter Path to append:  ")
file1=open(output_path,'a')
for i in os.listdir(input_path):
    if i.endswith('.txt'):
        file2=open(input_path+"\\"+i,'r')
        file1.write(file2.read()+'\n')
        file2.close()
file1.close()
print('Successfully append at '+os.path.abspath(output_path))
