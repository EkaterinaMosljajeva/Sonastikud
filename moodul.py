from random import *

def spisok(f):
    riik_peal={}
    peal_riik={}
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        riik_peal[k]=v
        peal_riik[v]=k
    return riik_peal,peal_riik

def poisk(f:str):
    riik_peal,peal_riik=spisok(f)
    p=int(input("Pealinn riigi järgi(1), riik pealinna järgi(2): "))
    try:
        if p==1:
            o=input("Sisestage riik: ")
            print(riik_peal[o])
        elif p==2:
            o=input("Sisestage pealinn: ")
            print(peal_riik[o])
    except:
        uus("riigid_pealinnad.txt")

def uus(x:dict,y:dict):
    r=input("Kirjutage riigi: ")
    while r in x:
        r=input("See riik on ")
    p=input("Kirjutage pealinn: ") 
    while p in y:
        p=input("See pealinn on ")
    x.update({r:p}) 
    salvesta(x,"riigid_pealinnad.txt")

def salvesta(x,f):
    riik=list(x.keys())
    linn=list(x.values())
    y=[]
    for i in range(len(x)):
        y.append(riik[i]+"-"+linn[i]+"\n")
    file=open(f,'w', encoding="utf-8-sig")
    file.writelines(y)

def paranda(x:dict,y:dict):
    while True:
        sona1=input("Kirjutage pealinn või riik, mida parandada: ")
        if sona1 in x:
            sona2=x.get(sona1)
            x.pop(sona1)
            y.pop(sona2)
            r=input("Sisestage õige riigi nimi: ")
            p=input("Sisestage pealinna õige nimi: ")
            break
        elif sona1 in y:
            sona2=y.get(sona1)
            x.pop(sona2)
            y.pop(sona1)
            r=input("Sisestage õige riigi nimi: ")
            p=input("Sisestage pealinna õige nimi: ")
            break
        else:
            print("Kirjutage õige riik või pealinn")
    x.update({r:p}) 
    y.update({p:r})
    salvesta(x,"riigid_pealinnad.txt")
    return x,y

def igra(x:dict):
    riik=list(x.keys())
    linn=list(x.values())
    ko=0
    try:
        n=int(input("Mitu korda: "))
    except:
        print("Vale Andmetüüp")
    for i in range(n):
        o=int(input("Kas arvame pealinnad(1) või riigid(2)?"))
        if o==1:
            rand=choice(riik)
            ind=riik.index(rand)
            print(linn[ind])
            sona=input("Sisesta: ")
            if sona in riik[ind]:
                print("Õige")
                ko+=1
            else:
                print("Vale")
        elif o==2:
            rand=choice(linn)
            ind=linn.index(rand)
            print(riik[ind])
            sona=input("Sisesta: ")
            if sona in linn[ind]:
                print("Õige")
                ko+=1
            else:
                print("Vale")
    print(f"{round(ko/n*100,1)}% vastused on õige ja {round(100-ko/n*100,1)}% on vale")
