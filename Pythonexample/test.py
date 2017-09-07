def File(work, CoffeeStock):
    if work == 'read':
        f = open("Coffee_Manage_file.txt", 'r')
        ReturnData = []
        while 1:
            line = list(f.readline())
            if not line:
                break
            if line[-1] == '\n':
                line.pop(-1)
            print(line)
            for i in range(0, len(line)):
                if line[i] == ' ':
                    break
                else:
                    i += 1
            ReturnData.append("".join(line[i+1:]))
        f.close()
        return ReturnData
    elif work == 'write':
        ManageData = {1:["Black_Coffee",CoffeeStock[0]], 2:["Milk_Coffee",CoffeeStock[1]], 3:["Gooooood_Coffee",CoffeeStock[2]]}
        print(ManageData)
        f = open("Coffee_Manage_file.txt", 'w')
        for i in ManageData:
            f.write("%s %s\n" %(ManageData[i][0], ManageData[i][1]))
            print("%s %s" %(ManageData[i][0], ManageData[i][1]))
        f.close()

Do = input()
print(File(Do, File(Do,[0,0,0])))