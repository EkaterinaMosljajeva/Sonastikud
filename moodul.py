def spisok(f:str):
    riik_peal={}
    peal_riik={}
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        riik_peal[k]=v
        peal_riik[v]=k
    file.close()
    return riik_peal,peal_riik

def poisk(f:str):
    riik_peal,peal_riik=spisok("riigid_pealinnad.txt")
    p=int(input("Kapital riigi järgi(1), riik kapitali järgi(2): "))
    if p==1:
        o=input("Sisestage riik: ")
        print(riik_peal[o])
    elif p==2:
        o=input("Sisestage pealinn: ")
        print(peal_riik[o])
    else:
        print()
