n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
if n<10:
 for i in range(0,n):
     x=int(input('Dati elementul='))
     a.extend([x])
print(a)



print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
z=a
z.insert(5,'    ')
print(z)
z.remove('    ')
a.reverse()
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator:')
print(a)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d)  afişează pe ecran doar componentele pare;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print(c)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
e=[]
nr=0
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        e.extend([y])
        nr+=1
print(sum(e)/nr)
print('f)  afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        f.extend([y])
print(f)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input('Dati elementul x='))
y=int(input('Dati elementul y='))
u=[]
for i in range(0,len(a)):
    if (a[i]>x)and(a[i]%y!=0):

        h=a[i]
        u.extend([h])
print(u)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x=int(input('Dati elementul x='))
y=int(input('Dati elementul y='))
u=[]
for i in range(0,len(a)):
    if (a[i]>x)and(a[i]<y):

        h=a[i]
        u.extend([h])
print(u)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
u=[]
for i in range(0,len(a)):
    if (a[i]%2!=0)and(a[i]<0):
        u.extend([i])

print(u)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
u=[]
for i in range(0,len(a)):
    if (a[i]>9) and((a[i]<100)):
        u.extend([i])

print(u)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=a
k[0]=min(k)
print(k)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=a
b=l.index(min(l))

l[b]=l[0]
print(l)

print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
n=int(input('Dati numarul de elemente din vector='))
t=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    t.extend([x])

u=[]
for i in range(0,len(t)):
    if (t[i]%2==0):
       w= t[i]
       u.extend([w])

print(u)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=int(input('Dati numarul de elemente din vector='))
t=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    t.extend([x])
u=[]
for i in range(0,len(t)):
    if (t[i]%3==0):
        w= t[i]
        u.extend([w])

print(u)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')
#pentru numere de 1,2 sau 3 cifre
n=int(input('Dati numarul de elemente din vector='))
t=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    t.extend([x])
u=[]
d=0
r=[]
y=0
for i in range(0,999):
        y+=1
        r.extend([y])
        
for i in range(0,len(t)):
    for o in range(0,len(r)):
       if t[i]%r[o]==0:
          d+=1     
    if d<=4:
         q=t[i]
         d=0
         u.extend([q])     
print(u)
