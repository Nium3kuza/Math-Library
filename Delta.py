'''
Created on 13 déc. 2017

@author: Nium3kuza
'''

from math import*

a=input("Prénom ?")
print("Bonjour",a)
print("Bienvenue sur le programme pour calculer Delta")

print("a=","b=","c=")
a =int(input())
b =int(input())
c =int(input())
d=((b*b)-(4*a*c))
print("d=",d)
if d<0:
    print("pas de solution possible dans ℝ")
else:
    if d>0:
        x1=(-b + sqrt(d))/(2*a)
        x2=(-b - sqrt(d))/(2*a)
        print("les deux racines sont x1=",x1,"et x2=",x2)
    else:
        print("l'unique racine est:",-b/(2*a))
    
 
    
   
    
    
