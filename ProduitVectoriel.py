'''
Created on 16 déc. 2017

@author: Nium3kuza
'''

from time import sleep

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

print("calcule du produit vectioriel en cours...")
sleep(2)

Wx=((Uy*Vz)-(Uz*Vy))
Wy=((Uz*Vx)-(Ux*Vz))
Wz=((Ux*Vy)-(Uy*Vx))

print("Wx=",Wx)
sleep(1)
print("Wy=",Wy)
sleep(1)
print("Wz=",Wz)

