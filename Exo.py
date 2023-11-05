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

for karakter in chenn:
    if karakter == "a":
        endeks = chenn.index(karakter)
        break

if endeks is not None:
    print("7: Premye karakter 'a' nan chenn se:", endeks)
else:
    print("Pa gen karakter 'a' nan chenn.")



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
 

#exo1 2eme partie
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