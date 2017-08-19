import time
def NotEnoughMoney(Money):
    print("Not enough Money")
    for i in range(0,3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)
    print("Automatic Change System")
    for i in range(0,3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)
    print("...Change: %d Won" % Money)

UserMoney = int(input("Please insert money: "))
while 1:
    if UserMoney <100:
            NotEnoughMoney(UserMoney)
            break
    print('''1. Black Coffee(100\\)
2. Milk Coffee (150\\)
3. Gooooooooooood Coffee (250\\)
4. Change
    '''
          )
    UserChoice = input("Choose: ")
    if UserChoice == '1':
        if UserMoney < 100:
            NotEnoughMoney(UserMoney)
            break
        else:
            print("\n<Black Coffee>\n")
            print("%d Won left\n" %(UserMoney-100))
            UserMoney = UserMoney - 100
            continue
    elif UserChoice == '2':
        if UserMoney < 150:
            NotEnoughMoney(UserMoney)
            break
        else:
            print("\n<Milk Coffee>\n")
            print("%d Won left\n" %(UserMoney-150))
            UserMoney = UserMoney - 150
            continue
    elif UserChoice == '3':
        if UserMoney < 250:
            NotEnoughMoney(UserMoney)
            break
        else:
            print("\n<Gooooooooooood Coffee>\n")
            print("%d Won left\n" %(UserMoney-250))
            UserMoney = UserMoney - 250
            continue
    elif UserChoice == '4':
        print("Change: %d Won" %UserMoney)
        break
    else:
        continue

