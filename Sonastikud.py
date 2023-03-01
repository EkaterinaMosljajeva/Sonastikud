from moodul import *
sonastik={}
spis1,spis2=spisok("riigid_pealinnad.txt")
while True:
    print()
    menu=int(input("1-Vaata nimekirja\n2-Leia pealinn riigi järgi ja vastupidi\n3-Lisage uus riik ja pealinn\n4-Parandage riiki/pealinna\n5-Teadmiste kontroll\n"))
    if menu==0:
        break
    elif menu==1:
        print(spis1)
    elif menu==2:
        poisk("riigid_pealinnad.txt")
    elif menu==3:
        riik_peal=uus(spis1,spis2)
    elif menu==4:
        spis1,spis2=paranda(spis1,spis2)
    elif menu==5:
        igra(spis1)
