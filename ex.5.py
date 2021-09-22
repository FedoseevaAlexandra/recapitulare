x=[1,2,3,4,5]
y=x
z=x[:3]
print('suma primelor 3 componente=',sum(z))
print('suma tuturor componentelor variabilei y=',sum(y))
prod=1
for i in range(0,len(x)):
    prod=prod*x[i]

print('produsul tuturor componentelor variabilei x=',prod)
print('valoarea absolută a componentei a treia a variabilei y=',abs(y[2]))
print('suma primelor componente ale variabilelor x şi y=',x[0]+y[0])