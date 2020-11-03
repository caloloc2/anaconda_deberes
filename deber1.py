# importa las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import random as r
import math as m

l=10 # l ∈ {3,4,5,...,10}
# crea la matriz de lxl llena de ceros
dots = np.zeros((l,l))
# setea el centro de la matriz
posx = 4 # variable q controla el eje x
posy = 4 # variable q controla el eje y
dots[posy, posx] = 1 # define el centro
final = False # controla si el proceso se ha finalizado o no
contador_movimientos = 0

def aleatorio():
    # funcion que genera un numero aleatorio entre 0 y 4
    return m.floor(r.random()*5)

def vecinos(x, y):
    # funcion que dependiendo el punto donde se encuentre, revisa si existe
    # espacios disponibles (0) para poder generar otro nuevo movimiento
    retorno = False
    contador = 0

    # para el ejey verifica que el valor este entre 0 y 8
    # y verifica si existe posicion disponible (0)
    if ((y>=0) and (y<=(l-1))):
        if (y!=0) and (y!=(l-1)):
            if (dots[(y-1), x]==0):
                contador += 1        
            elif (dots[(y+1), x]==0):
                contador += 1
        elif (y==0):
            if (dots[(y+1), x]==0):
                contador += 1
        elif (y==(l-1)):
            if (dots[(y-1), x]==0):
                contador += 1

    # para el ejex verifica que el valor este entre 0 y 8
    # y verifica si existe posicion disponible (0)
    if ((x>=0) and (x<=(l-1))):
        if (x!=0) and (x!=(l-1)):
            if (dots[y, (x-1)]==0):
                contador += 1        
            elif (dots[y, ( x+1)]==0):
                contador += 1
        elif (x==0):
            if (dots[y, (x+1)]==0):
                contador += 1
        elif (x==(l-1)):
            if (dots[y, (x-1)]==0):
                contador += 1
        
    if (contador>=1): # si existe, por lo menos 1 sitio disponible (0), retorna Verdadero
        retorno = True
    
    return retorno

while (not final):
    # funcion principal que se ejecuta gasta que la variable Final sea Verdadera, es decir, ya no existen mas movimientos posibles
    mov = aleatorio() # obtiene el valor aleatorio    
        
    if (mov!=0): # valida que el valor obtenido sea diferente de cero
        tempx = posx # crea una posicion temporal de donde posiblemente iria el proximo movimiento en x
        tempy = posy # crea una posicion temporal de donde posiblemente iria el proximo movimiento en y

        if (mov==1): # movimiento arriba
            tempy -=1              
        elif (mov==2): # movimiento abajo            
            tempy +=1            
        elif (mov==3): # movimiento izquierda            
            tempx -=1            
        elif (mov==4): # movimiento derecha            
            tempx +=1            

        # verifica que no se haya sobrepasado de los limites de la matriz
        if (((tempx>=0) and (tempx<=(l-1)))  and  ((tempy>=0) and (tempy<=(l-1)))):
            if (dots[tempy, tempx]==0): # si la posicion nueva tiene valor (0) es decir esta disponible
                # grafica el movimiento realizado
                plotx = [posx, tempx]
                ploty = [posy, tempy]
                plt.plot(plotx, ploty, marker='o', linestyle="-", color='b')                

                # guarda la nueva posicion y setea el valor como ocupado (1)
                posx = tempx
                posy = tempy
                dots[posy, posx] = 1
                contador_movimientos += 1
            else: # si el nuevo movimiento esta como ocupado (1)
                # verifica si existe mas movimientos posibles en la posicion nueva
                if (not vecinos(posx, posy)): # si no es asi (False), da por terminado el proceso ya que no existe posibles movimientos
                    final = True            
        #print dots

print("Se realizaron ", contador_movimientos)
# grafica las posicion inicial (centro [4,4])
plt.plot(posx, posy, marker='o', linestyle="", color='r', markersize=16)
# grafica las posicion final obtenida
plt.plot(4, 4, marker='x', linestyle="", color='r', markersize=8)
# muestra el grafico
plt.show()