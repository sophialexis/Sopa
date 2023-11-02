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
    print("Premye karakter 'a' nan chenn se:", endeks)
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
 


