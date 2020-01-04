def karsilastir(gelen,aranan):
    arrayx=list(gelen)
    arrayaranan=list(aranan)
    sayac=0
    if len(gelen)>len(aranan):
        for i in range(0,len(aranan)):
            if(arrayx[i]==arrayaranan[i]):
                sayac=sayac+1
            else:
                pass
    elif len(gelen)<len(aranan):
        for i in range(0,len(gelen)):
            if(arrayx[i]==arrayaranan[i]):
                sayac=sayac+1
            else:
                pass
    if(sayac>0):
        print("did you mean?",gelen);
        f0=open("bulunan.txt","a",encoding="utf-8")
        f0.write(gelen)
        f0.close()
    if(sayac==0):
        pass
aranankelime=input("Lütfen aranankelimeyi giriniz")
f=open("deneme.txt",encoding="utf-8")
f.seek(0)
kelimeler=f.readlines()
for i in kelimeler:
    karsilastir(i,aranankelime)