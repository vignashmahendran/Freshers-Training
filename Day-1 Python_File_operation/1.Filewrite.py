text=input("Please Enter Text To be save in a File :  ")
file_name=input("Please Enter File name with path :  ")
try:

    with open(file_name,'w') as input:
        input.write(text)
    print("File Created Successfully")

except Exception as e:
    print("There is a Problem in Writing File"+str(e))
    