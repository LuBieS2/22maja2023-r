#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2023/Informatyka/EINP-R2-100-2305.pdf
file=open("przyklad.txt", "r")
words=list(map(str.strip, file.readlines()))
#4.1
print("#4.1")
wk=[]
for word in words:
    w_count=0
    k_count=0
    for letter in word:
        if letter=="w":
            w_count=w_count+1
        if letter=="k":
            k_count=k_count+1
    if w_count==k_count:
        wk.append(word)
for i in wk:
    print(i)
#4.2
print("#4.2")
for word in words:
    w=word.count("w")
    a=word.count("a")
    k=word.count("k")
    c=word.count("c")
    j=word.count("j")
    e=word.count("e")
    #print(w,a,k,c,j,e)    
    wakacje=[w,a,k,c,j,e]
    print(wakacje)
    w_count=0
    for i in wakacje:
        w_count+=i
    #print(w_count)
    mi=min(wakacje)
    maks=max(wakacje)
  
    if wakacje[1]<2:
        w_count=0
    elif (wakacje[1]==maks or wakacje[1]>maks/2)and mi>=wakacje[1]/2:
        w_count=int(wakacje[1]/2)
    else:
        w_count=mi
    #print(w, a, k, c, j, e)
    print(w_count)
#4.3
print("#4.3")
for word in words:
    counter=0
    wakcje=["w", "a", "k", "a", "c", "j","e"]
    wrd=[]
    for i in word:
        wrd.append(i)
    wje=[]
    #print(wrd)
    for i in wrd:
        if i in wakcje:
            wje.append(i)
        #else:
            #wrd.remove
    wje_c=wje.copy()
    for i in wje:
        if i !="w":
            wje_c.remove(i)
            counter+=1
        else:
            break
    if len(wje_c)>=7:
        #print(wje_c[0])
    #print(wje, counter)
        if wje_c[1]!="a":
            wje_c.pop(1)
    print(wje_c)