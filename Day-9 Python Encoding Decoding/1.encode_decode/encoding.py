text_file=input("enter the text file path: ")
decode_f=input("enter the input file encoding format like UTF-8,UTF-16: ")
write_file=input("enter the output file path: ")
encode_f=input("enter the output file encoding format like UTF-8,UTF-16: ")
try:
    with open(text_file,'r',encoding=decode_f) as file:
        with open(write_file,'w',encoding=encode_f) as write_file:
            write_file.write( file.read())
    print("Format change successful")
except Exception as e:
    print(e)        