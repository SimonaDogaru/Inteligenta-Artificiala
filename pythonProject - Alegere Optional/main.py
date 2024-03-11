

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    packet1=[0,0,0,0]# Programare bazată pe reguli , Tehnici de programare pe platforme mobile , Aspecte computaţionale în teoria numerelor, Proiectarea jocurilor
    packet2=[0,0,0,0]# Psihologia comunicării profesionale în domeniul IT-lui, Cloud Computing,Interacțiune om-calculator, Analiza reţelelor media sociale
    packet3=[0,0,0,0]# Reţele Petri şi aplicaţii, Smart Card-uri şi Aplicaţii, Inginerie software specifică automobilelor, Introducere în Internetul lucrurilor

    print("Salut, student curios!\nAceasta aplicatie are ca scop oferirea unei recomandari de optionale pentru anul 3 sem 2")
    print("Te rugam sa raspunzi la urmatoarele intrebari!")

    #packetul 1

    ok=0
    while (ok==0):
        print("Este important pentru tine sa vezi imediat resultatul efortului tau?\n  DA\n  NU")
        raspuns= input()
        if raspuns == 'DA' or raspuns =='NU':
            ok = 1
        else:
            print("Te rugam alege intre 'DA' sau 'NU'")

    if raspuns == 'DA':
        packet1[0]+=1
        packet1[1]+=2
        packet1[2]+=0.5
        packet1[3]+=2
    else:
        packet1[0]+=2
        packet1[1]+=1
        packet1[2]+=2
        packet1[3]+=1

    ok = 0
    while (ok == 0):
        print("Pe viitor te vezi lucrand pe parte de cercetare, stiinta?\n  DA\n  NU")
        raspuns = input()
        if raspuns == 'DA' or raspuns == 'NU':
            ok = 1
        else:
            print("Te rugam alege intre 'DA' sau 'NU'")
    if raspuns == 'DA':
        packet1[0] += 2
        packet1[1] += 0.5
        packet1[2] += 2
        packet1[3] += 1
    else:
        packet1[0] += 1
        packet1[1] += 2
        packet1[2] += 0.5
        packet1[3] +=2

    #packetul 2
    # Psihologia comunicării profesionale în domeniul IT-lui, Cloud Computing,
    # Interacțiune om-calculator, Analiza reţelelor media sociale

    ok = 0
    while (ok == 0):
        print("Pe viitor te vezi mai mutl:\n  (1) un bun expert in partea de tech sau (2) un bun expert in facilitarea managementului echipei?")
        raspuns = input()
        if raspuns == '1' or raspuns=='(1)' or raspuns == '2' or raspuns == '(2)':
            ok = 1
        else:
            print("Te rugam alege intre '1' sau '2'")
    if raspuns == '1' or raspuns=='(1)':
        packet2[0] += 0.5
        packet2[1] += 2
        packet2[2] += 2
        packet2[3] += 1
    else:
        packet2[0] += 2
        packet2[1] += 0.5
        packet2[2] += 1
        packet2[3] +=2

    ok = 0
    while (ok == 0):
        print("In general, iti place sa iti imbunatatesti skilurile e interactiune umana?\n  DA\n  NU")
        raspuns = input()
        if raspuns == 'DA' or raspuns == 'NU':
            ok = 1
        else:
            print("Te rugam alege intre 'DA' sau 'NU'")
    if raspuns == 'DA':
        packet2[0] += 2
        packet2[1] += 0.5
        packet2[2] += 1
        packet2[3] += 2
    else:
        packet2[0] += 0.5
        packet2[1] += 2
        packet2[2] += 1.5
        packet2[3] += 1
#packet3
print(packet1, packet2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
