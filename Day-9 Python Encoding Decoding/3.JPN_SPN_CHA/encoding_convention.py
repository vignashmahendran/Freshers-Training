with open("jpn.txt","r",encoding="shift jis") as input_file:
    with open('jpn_out.txt',"w+",encoding="utf-8") as output_file:
        output_file.write(input_file.read())
        ipstr=input_file.read()
        print(ipstr)
        opstr=output_file.read()
        print(opstr)
        if(ipstr==opstr):
            print("The japanese text is coming out correctly")
        else:
            print("The text in Japanese not correctly")

with open("esp.txt","r",encoding="windows 1256") as input_file:
    with open('esp_out.txt',"w+",encoding="utf-8") as output_file:
        output_file.write(input_file.read())
        ipstr=input_file.read()
        print(ipstr)
        opstr=output_file.read()
        print(opstr)
        if(ipstr==opstr):
            print("The arabic text is coming out correctly")
        else:
            print("The text in arabic not correctly")

with open("fra.txt","r",encoding="windows 1253") as input_file:
    with open('fra_out.txt',"w+",encoding="utf-8") as output_file:
        output_file.write(input_file.read())
        ipstr=input_file.read()
        print(ipstr)
        opstr=output_file.read()
        print(opstr)
        if(ipstr==opstr):
            print("The greek text is coming out correctly")
        else:
            print("The text in greek not correctly")

with open("chn.txt","r",encoding="big5-hkscs") as input_file:
    with open('chn_out.txt',"w+",encoding="utf-8") as output_file:
        output_file.write(input_file.read())
        ipstr=input_file.read()
        print(ipstr)
        opstr=output_file.read()
        print(opstr)
        if(ipstr==opstr):
            print("The chinese text is coming out correctly")
        else:
            print("The text in chinese not correctly")

with open("rus.txt","r",encoding="euc-kr") as input_file:
    with open('rus_out.txt',"w+",encoding="utf-8") as output_file:
        output_file.write(input_file.read())
        ipstr=input_file.read()
        print(ipstr)
        opstr=output_file.read()
        print(opstr)
        if(ipstr==opstr):
            print("The korean text is coming out correctly")
        else:
            print("The text in korean not correctly")


