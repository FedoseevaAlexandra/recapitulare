v=[500,600,532,789,567,980,658]
print('venitul săptămânal al întreprinderii=',sum(v))
print('media venitului zilnic=',sum(v)/len(v))
print(' ziua în care s-a obţinut cel mai mare venit este ziua nr',v.index((max(v)))+1)
print('ziua cu venitul cel mai mic este ziua nr', v.index(min(v))+1)
