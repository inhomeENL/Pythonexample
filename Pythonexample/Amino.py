import random
while 1:
    i = 20
    List = {1:["Glycine","Gly","G"], 2:["Alanine","Ala","A"], 3:["Proline","Pro","P"], 4:["Valine","Val","V"],
            5:["Leucine","Leu","L"], 6:["Isoleucine","Ile","I"], 7:["Methionine","Met","M"], 8:["Phenylalanine","Phe","F"],
            9:["Tyrosine","Tyr","Y"], 10:["Tryptophan","Try","W"], 11:["Serine","Ser","S"], 12:["Threonine","Thr","T"],
            13:["Cysteine","Cys","C"], 14:["Asparagine","Asn","N"], 15:["Glutamine","Gln","Q"], 16:["Lysine","Lys","K"],
            17:["Arginine","Arg","R"], 18:["Histidine","His","H"], 19:["Asparate","Asp","D"], 20:["Glutamate","Glu","E"]}
    KeyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    while 1:
        pick = random.randint(1,len(KeyList))
        i = i - 1
        print("Left: %d" %i)
        print(List[KeyList[pick-1]][random.randint(0,2)])
        KeyList.remove(KeyList[pick-1])
        Delay = input("Next(Press ENTER)\n")
        if i == 0:



            break
    Do = input("Re?(y/n): ")
    if Do == 'y' or Do == 'Y':
        continue
    else:
        break