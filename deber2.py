import random 
import numpy as np 
import matplotlib.pyplot as plt 

prob = [0.5, 0.5] # probabilidad del 50% de moverse a la izquierda o derecha
n = 5 # absorbing barrier

pos_actual = 0 # posicion inicial establecida en cero
pos_contador = 0 # contador de pasos
iteraciones = True # bandera para iteraciones

while(iteraciones): # itera mientras la variable sea verdadera
    rr = np.random.random() # obtiene un valor randomico
    if (rr > prob[0]): # derecha (dependiendo de la probabilidad asignada) 
        pos_actual += 1
    else: # izquierda
        pos_actual -= 1
    
    pos_contador += 1

    if (pos_actual==n): # si se encuentra con absorbing barrier        
        iteraciones = False # termina las iteraciones

print("Se requirieron "+str(pos_contador)+" pasos hasta la absorning barrier en n="+str(n))