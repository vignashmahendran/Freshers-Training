
#getting list of name
names=[]
while(True):
    input1=input("Enter name or enter Exit to terminate :")
    if(input1.lower()=="exit"):
        break
    names.append(input1)
sub_str=input("Enter letter to start in names :")

newlist=lambda list1,sub :[x for x in list1 if sub == x[0]]
print("------Names-------")

for i in newlist(names,sub_str):
    print(i)