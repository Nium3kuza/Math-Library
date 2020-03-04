'''
Created on 16 déc. 2017

@author: Nium3kuza
'''

a=input("Prénom ?")
print("Salut",a)
print("Bienvenue sur le programme PDVec, ce programme calcul le produit vectoriel")

from math import*

print("Ux=","Uy=","Uz=")

Ux=int(input())
Uy=int(input())
Uz=int(input())

print("Vx=","Vy=","Vz=")

Vx=int(input())
Vy=int(input())
Vz=int(input())

Wx=((Uy*Vz)-(Uz*Vy))
Wy=((Uz*Vx)-(Ux*Vz))
Wz=((Ux*Vy)-(Uy*Vx))

print("Wx=",Wx)
print("Wy=",Wy)
print("Wz=",Wz)

