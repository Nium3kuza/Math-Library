'''
Created on 26 déc. 2017

@author: Nium3kuza
'''
from math import*

# test de la fonction table
nb=input("entrer un nombre")
def table(nb, max=20):
    i = 0
    while i<max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1