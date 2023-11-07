from random import choice
import string
import random


print("str")
#exo 1
a = "BONJOUR"
a = a.lower()
print("1: ",a)


#exo2
t="dlo se lavi "
ta= t.split()
print("2: ",ta)

#xo3
ma="mete premye let yo an miniskil "
ma=' '.join(m.capitalize()  for m in ma.split())
print("3:",ma)

#exo4
rekipere=" ranplase tout karakte"
o= rekipere.split()
v= [mo[0] for mo in o]
s = ''.join(v)
print("4: ", s)

#exo5
ran=" chenn karakte yo la"
chenn=ran.replace("a","@")
print("5: ", chenn)

#xo6
devan= "afiche "
va= ''.join(reversed(devan.upper()))
print("6: ", va)


#exo7
chenn = "endeks la  "
endeks = None

for karakte in chenn:
    if karakte == "a":
        endeks = chenn.index(karakte)
        break

if endeks is not None:
    print("7: Premye karakte 'a' nan chenn se:", endeks)
else:
    print("Pa gen karakte 'a' nan chenn.")



#exo8
ind="andann"
af= "a"
k = ind.count(af)
print("8: ",k)

#exo9
k="lis la"
lis=[]
li="a"
longe=len(k)
l=0
for mn in range(longe):
    if k[l]=="a":   
        lis.append(l)
        l +=1
       
print("9: ", lis)


#exo10
so= "retire espas nan yon chenn."
lami= so.replace (" ","")
print("10: ", lami) 
print("List")



# #exo1 2eme partie


k= "kreye yon lis elememan."
n=10
lis=[i for i in range (n+1) if i%2==0]
print("1:" , lis)

#exo2
lis_antye = [1, 2, 3, 4, 5]
lis_chenn = [str(x) for x in lis_antye]
print("2: ",lis_chenn)

#exo3
lis = ["pom", "banann", "kann", "fwi"]
majiskil = [las.upper() for las in lis]
print("3: ",majiskil)

#exo4
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,24,27,30]
divizib_pa_3 = [l[i] for i in range(len(l)) if i % 3 == 0]
print("4: ",divizib_pa_3)

#exo5
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lis_tipl = [(li[i], li[i + 1], li[i + 2]) for i in range(0, len(li), 3)]
print("5: ",lis_tipl)

#exo6
lis_avek_doublon = [1, 2, 2, 3, 4, 4, 5, 6, 4,6,"A","A"]
lis_san_doublon = list(set(lis_avek_doublon))
print(lis_san_doublon)

#exo 7
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lisa = [t for t in lis1 if t in lis2]
print("7: ",lisa)

#exo8
lis1= [1,2,3,4,5]
lis2= [3,4,5,6,7]
new_lis= list(set(lis1) ^ set (lis2) )
print ("8: " , new_lis)

#exo9
dict={ 'f': '6', 'r': '18', 'j': '3'}
pilot= list(dict.keys())
avion= list(dict.values())
print ("9: ", pilot)
print ("9: ", avion)

#exo10
lister1 = [1,2,3,4,5]
lister2= [3,4,5,6,7]
lister3= [5,6,7,8,9]
lister_aficher= list(set(lister1)|set(lister2) | set(lister3))
print("10:" , lister_aficher)

print("Dict")
# exo 1
pwa= {'r1': 'm2' , 'p1': 'd2' }
diri_kole= list ( pwa.values())
print(" 1:" , diri_kole)

# exo 2
vetman= input ("ekri yon vale:")
if vetman.startswith("{") and vetman.endswith("}"):
    print(" vale a korek.")
else:
        print ("vale a pa korek.")


#exo 3
pwodui= {'r1': 'm2' , 'p1': 'd2' }
manje_lokal= list ( pwodui.keys())
print(" 3:" , manje_lokal)

#exo4
liv={'ji1': 'manje2' ,  'bwe1': 'dlo2'}
for bibliyotek in liv.values():
    print("4:" , bibliyotek)

    #exo5
jaden_manje = {'pi': '3', 'ke': 'we', 'sa': '4'}

love = {}
for live, lave in jaden_manje.items():
    love[live] = lave
print("5 :", jaden_manje)
print("5 :", love)

#exo6
zazou= {'a1': 's1'  , 'q1': 'f2','d1': "tor"}
for sisi, wewe in zazou.items():
    if isinstance ( wewe, str): 
        zazou[sisi]= f"_{wewe}_"
print("6:" , zazou)

#exo7
bebe_diksyone = { 'cle1': '123', 'cle2': 'abc', 'cle3': '456', 'cle4': 'def', 'cle5': '789'}
val_q ={ou : oui for ou, oui in bebe_diksyone.items() if oui.isdigit()}
print("7: ",val_q)

#exo8
melomann= { 'mizik1': 'chant1', 'dans2': 'vwa2', 'piblik3': 'anbyans3'}
atis_entenasyonal =  list(melomann.items())
print ("8: " , melomann)
print ("8: ", atis_entenasyonal)


#exo9
lekol= [("a",1) , ("b", 2)]
elev = (lekol)
print("9: ",lekol)
print("9: ",elev


# print(...........................................................)
# print(.............................................................)

# print(............................Fonksyon............................)

#exo1

def tounen_enves (mo):
    enves= mo[::-1]
    return enves
mo_input="Hello"
enves= tounen_enves ( mo_input)
print("1: " , enves)

#exo2

def kod_jenere_aleyatwaman(n):
    karakte_alfabetik=string.ascii_letters
    kod= ''.join(choice(karakte_alfabetik) for _ in range(n))
    return kod 
jenere_aleyatwaman= kod_jenere_aleyatwaman(5)
print("2:" , jenere_aleyatwaman)

    #exo3
def toto(o):
    tete = string.ascii_letters
    kod_p= ''.join(random.sample( tete, o))
    return kod_p
kod_aleyatwa= toto(5)
print(" 3:" , kod_aleyatwa)

#exo 4
def bouyon_boy (ye):
    dispo= string.digits + string.ascii_letters
    if ye > len ( dispo):
        print(" kantite depase") 
    gigi = ''.join (random.sample( dispo, ye))
    return gigi
bouyon = bouyon_boy(5)
print("4:" , bouyon)

#exo5
def krem_glase(vaniy):
    akseptab= string.ascii_letters + string.digits + "_"
    achte = ''.join([''.join (co for co in sey if co in akseptab) for sey in vaniy])
    return achte
kokoye_vaniy= ["frez" , "rezen"]
achte = krem_glase (kokoye_vaniy)
print(" 5: ", achte)


#exo6

def separe_let_vigil( mo, vigil):
    mo_separe= vigil.join(mo)
    return mo_separe
mo= " plaisanterie"
vigil= "-"
mo_separe= separe_let_vigil (mo, vigil)
print("6:" ,mo_separe)


   #exo 7 
def kript_alfa( grande):
    choz= "abcdefghijklmnopqrstuvwxz"
    alfa_kript= " _" .join(str(choz.index(let) + 1) for let in grande)
    return alfa_kript 
grande="cordialement"
kript=kript_alfa(grande)
print("7: " , kript)

#exo8
def anmweyy(mapo):
    way = "abcdefghijklmnopqrstuvwxyz"  
    nou = [way[int(index) - 1] for index in mapo.split('-')]
    wii = ''.join(nou)
    return wii
mapo = "10-25-5-11"
wii = "anmweyy (wii)"
print("8: ", wii)

# exo9
def sesa(bwa, bwa2):
    return (bwa, bwa2)
jodya = "toujou"
jodya2 = "pafe"

mewi = sesa(jodya, jodya2)
print("9:", mewi)

# exo10
def levanjil(fidel):
    paste = fidel.split()
    priye = []

    for medite in paste:
        if medite != "":
            priye.append(medite[0])

    return ''.join(priye)
fre = input("antre nom an: ")
kris = levanjil(fre)
print("10:" , kris)





    






   















