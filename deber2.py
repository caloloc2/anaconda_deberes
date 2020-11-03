import random 
import numpy as np 
import matplotlib.pyplot as plt 

prob = [0.5, 0.5] # probabilidad del 50% de moverse a la izquierda o derecha
n = 2 # numero de pasos

inicio = 0 # inicio establecido en cero
positions = [inicio]

rr = np.random.random(n)
print(rr)
izqp = rr < prob[0]
derp = rr < prob[1]
print(izqp)
# for i_izq, i_der in zip(izqp, derp):
#     izquierda = i_izq and positions[-1] > 1