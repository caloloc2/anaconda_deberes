from mpl_toolkits import mplot3d
import random 
import numpy as np 
import matplotlib.pyplot as plt 

dims = 3 # dimensiones 
step_n = 1000 # numero de pasos
step_set = [-1, 0, 1] # seteo de posibles valores para movimientos
origin = np.zeros((1,dims)) # punto de inicio segun la dimension (0,0,0)
back_origin = 0

step_shape = (step_n,dims) # limites para seleccion de valores
steps = np.random.choice(a=step_set, size=step_shape) # seleccion de valores aleatorios dentro de step_set y con step_shape como limites

for st in steps:    
    if np.all((st==0)):
        back_origin+=1

if (back_origin>0):
    print("Probabilidad de regresar al origen: ", (step_n/back_origin))
    print("Pólya's Random Walk Constants (3d):", (0.340537*100))
else:
    print("Muy pocos numeros de pasos.")

path = np.concatenate([origin, steps]).cumsum(0) # concatenacion de valores obtenidos (caminata)
start = path[:1] # obtiene el inicio de la caminata
stop = path[-1:] # obtiene el final de la caminata

fig = plt.figure(figsize=(10,10),dpi=200)
ax = fig.add_subplot(111, projection='3d')
ax.grid(True)
ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter3D(path[:,0], path[:,1], path[:,2], c='blue', alpha=0.25, s=1)
ax.plot3D(path[:,0], path[:,1], path[:,2], c='blue', alpha=0.5, lw=0.5)
ax.plot3D(start[:,0], start[:,1], start[:,2], c='red', marker='+')
ax.plot3D(stop[:,0], stop[:,1], stop[:,2], c='black', marker='o')
plt.title('Ejercicio '+str(dims)+' dimensiones')

nombre_archivo = 'plots/deber3_plot_'+str(dims)+'d.png'
plt.savefig(nombre_archivo, dpi=250);
print("Imagen exportada en archivo => "+nombre_archivo)