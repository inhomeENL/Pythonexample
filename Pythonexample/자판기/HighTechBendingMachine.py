import os

def MenuOut(AdminCode):
    File('read')
    if AdminCode == 0:
        for ji in range(len(MenuListNum)):
            if MenuList[ji][2] == 0:
                print("%d. %s (%d) - SOLD OUT" % (MenuListNum[ji], MenuList[ji][0], MenuList[ji][1]))
            print("%d. %s (%d)" %(MenuListNum[ji], MenuList[ji][0], MenuList[ji][1]))
        print("%d. Change (Exit)\n" %(len(MenuListNum)+1))
    else:
        for j in range(len(MenuListNum)):
            print("Stock #%-3d ID: %-15s  Price: %5d  Stock left: %4d"
                  %(MenuListNum[j], MenuList[j][0], MenuList[j][1], MenuList[j][2]))
        print("")

def MenuChange():
    while 1:
        Mode = input("Menu Manage Mode... \n\nMenu/Stock : ")
        if Mode == 'Menu':
            ChangeWay = input("Add/Del/Change? : ")
            if ChangeWay == "Add":
                NewMenuID = input("\nNew Menu: ")
                NewMenuPrice = int(input("New Menu Price : "))
                NewMenuStock = int(input("New Menu Stock: "))
                NewMenu = [NewMenuID, NewMenuPrice, NewMenuStock]
                MenuList.append(NewMenu)
                MenuListNum.append(len(MenuListNum)+1)
            elif ChangeWay == 'Change':
                ChangeWhat = input("Name/Price? : ")
                if ChangeWhat == 'Name':
                    ChangeNameNum = int(input("Changed Menu #? : "))
                    ChangeName = input("Menu Name: %s\nChanged Name? : " %MenuList[ChangeNameNum-1][0])
                    MenuList[ChangeNameNum-1][0] = ChangeName
                elif ChangeWhat == 'Price':
                    ChangePriceNum = int(input("Changed Menu #? :"))
                    ChangePrice = input("Menu Price: %s\nChanged Price?: " %MenuList[ChangePriceNum-1][1])
                    MenuList[ChangePriceNum-1][1] = int(ChangePrice)
            elif ChangeWay == 'Del':
                Choice = input("ID or #? : ")
                if Choice == 'ID':
                    DelMenuID = input("Deleted Menu ID: ")
                    MenuListNum.remove(len(MenuListNum))
                    for ii in range(0, len(MenuList)-1):
                        if MenuList[ii][0] == DelMenuID:
                            MenuList.pop(ii)
                elif Choice == "#":
                    DelMenuNum = int(input("Deleted Menu Number : "))
                    MenuListNum.remove(len(MenuListNum))
                    MenuList.pop(DelMenuNum-1)
        elif Mode == 'Stock':
            Choice = input("ID or #? : ")
            Hold = 0
            if Choice == "ID":
                StockChangeID = input("Changed Menu ID : ")
                for ij in range(0, len(MenuList)):
                    if MenuList[ij][0] == StockChangeID:
                        Hold = int(ij)
                        break
            elif Choice == "#":
                StockChangeNum = int(input("Changed Menu Number : "))
                Hold = StockChangeNum - 1
            StockChange = int(input("Current Stock: %s\nAdditional Stock : " %MenuList[Hold][2]))
            MenuList[Hold][2] = MenuList[Hold][2] + StockChange
        os.system('cls')
        MenuOut(1)
        UserChoiceI = input("Anymore Changes?(y/n) : ")
        if UserChoiceI == "y":
            continue
        else:
            File('write',MenuList, MenuListNum)
            os.system('cls')
            return

def File(do, MenuList = [], MenuListNum = []):
    if do == 'write':
        f = open("Menu_Stock_1.txt", 'w', encoding='utf-8')
        for i in range(0, len(MenuListNum)):
            f.write("%d/%s/%d/%d\n" % (MenuListNum[i], MenuList[i][0], MenuList[i][1], MenuList[i][2]))
        f.close()
    elif do == 'read':
        try:
            f = open("Menu_Stock_1.txt", 'r', encoding='utf-8')
            MenuList = []
            MenuListNum = []
            while 1:
                line = f.readline()
                if not line:
                    break
                Data = line.strip().split('/')
                MenuListNum.append(int(Data[0]))
                Data.pop(0)
                Data[1] = int(Data[1])
                Data[2] = int(Data[2])
                MenuList.append(Data)
            f.close()
            return (MenuList, MenuListNum)
        except:
            File('write',[['Black Coffee', 100, 20]],[1])
            return 0


MenuListNum = []
MenuList = []
(MenuList, MenuListNum) = File('read')
while 1:
    os.system('cls')
    Money = (input("Money please : "))
    if Money == 'admin':
        os.system('cls')
        print("Admin Excess code...\n")
        UserCode = input()
        if UserCode == 'HellYeah':
            os.system('cls')
            print("Admin mode on...\n")
            MenuOut(1)
            MenuChange()
        else:
            continue
    else:
        while 1:
            while 1:
                Breakout = 0
                for i in range(len(MenuList)):
                    Minimum = MenuList[0][1]
                    if Minimum >= MenuList[i][1]:
                        Minimum = MenuList[i][1]
                os.system('cls')
                Money = int(Money)
                if Money < Minimum:
                    print("Money left: %s" %Money)
                    print("Change: %d" %Money)
                    break
                print("Money left : %d" %Money)
                MenuOut(0)
                UserChoice = int(input("Coffee # : "))
                if UserChoice == len(MenuListNum)+1:
                    print("User Choice: Change...\nChange : %d" %Money)
                    Breakout = 0
                    break
                if Money < MenuList[UserChoice-1][1]:
                    print(Money)
                    print(MenuList[UserChoice-1][1])
                    print("Not Enough Money....\nChange: %d" %Money)
                    Breakout = 0
                    break
                if MenuList[UserChoice-1][2] <= 0:
                    print("Not Enough Coffee.... SOLD OUT")
                    Breakout = 1
                    break
                print("Coffee out.... %s ready" %MenuList[UserChoice-1][0])
                MenuList[UserChoice-1][2] = MenuList[UserChoice-1][2] - 1
                Money = Money - MenuList[UserChoice-1][1]
                File('write', MenuList, MenuListNum)
            if Breakout == 1:
                OtherMenu = input("Other Menu? (y/n) : ")
                if OtherMenu == 'y':
                    continue
                else:
                    break
            else:
                break
    Try = input("More Money? (y/n) : ")
    if Try == 'y':
        continue
    else:
        break


