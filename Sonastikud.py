from moodul import *
sonastik={}
file=open("riigid_pealinnad.txt",'r', encoding="utf-8-sig")
while True:
    menu=int(input("1-Vaata nimekirja\n2-Leia pealinn riigi järgi ja vastupidi\n"))
    if menu==0:
        break
    elif menu==1:
        spisok(sonastik)
    elif menu==2:
        poisk("riigid_pealinnad.txt")
