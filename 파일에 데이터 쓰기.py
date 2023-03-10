with open("프밍실습.txt", "r") as my_file:
    i = 1
    while 1:
        line = my_file.readline()
        if not line:
            break
        print(str(i)+":"+line.replace("\n",""))
        i=i+1
