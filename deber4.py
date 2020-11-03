import numpy as np
import math

def genera_matriz(y, x, p):
    # crea un matriz (con bordes de cero para facilidad de calculo)
    grid = np.zeros((y+2, x+2))

    # llenado de la matriz segun la probabilidad
    for cell in np.nditer(grid[1:-1, 1:-1], op_flags=['readwrite']):
        cell[...] = 0 if np.random.random()<p else 1

    return grid # retorno de matriz

def encuentra_clusters(matriz):
    # verifica el numero de elementos que no son cero
    num_of_ones = np.count_nonzero(matriz)    
    ids = np.arange(num_of_ones) # lista de indices de los puestos ocupados o con 1
    coords = [list(x) for x in np.argwhere(matriz>0)] # obtiene las coordenadas dentro de la matriz sin contar los bordes    
    while True:
        cw = []
        for i in np.arange(ids.size):
            # extrae las coordenadas en la ubicacion actual
            y,x = coords[i]

            # Solo si el vecino esta ocupado, cambiamos de etiqueta
            # de la ubicacion actual
            if matriz[y-1][x]==1 and matriz[y][x-1]==0:
                ids[i] = ids[coords.index([y-1,x])]
            elif matriz[y][x-1]==1 and matriz[y-1][x]==0:
                ids[i] = ids[coords.index([y,x-1])]

            # Si los dos vecinos estan ocupados o con 1
            elif matriz[y-1][x]==1 and matriz[y][x-1]==1:
                first_neighbor_id = ids[coords.index([y-1,x])]
                second_neighbor_id = ids[coords.index([y,x-1])]
                ids[i] = np.min([first_neighbor_id, second_neighbor_id])

                if first_neighbor_id!=second_neighbor_id:
                    cw.append([first_neighbor_id,second_neighbor_id])

        # Si no hay etiquetas cierra el ciclo o funcion
        if cw==[]:
            break
        # caso contrario encuentra las etiquetas
        else:
            for id1,id2 in cw:
                wrong_id = np.max([id1,id2])
                correct_id = np.min([id1,id2])
                ids[ids==wrong_id] = correct_id

    return coords,ids # retorna las coordenadas e indices

def existe_percolacion(coordenadas, indices, y, x):
    # encuentra las ids unicas de las coordenadas enviadas    
    coordenadas_clusters = []
    for idx in np.unique(indices):
        coordenadas_clusters.append([coords[k] for k in range(len(indices)) if indices[k]==idx])

    # busqueda de posibles percolaciones
    hacia_arriba = False
    izq_derecha = False
    for cluster in coordenadas_clusters:
        cluster = np.array(cluster).T
        if (1 in cluster[0]) and (y in cluster[0]):
            hacia_arriba = True
        if (1 in cluster[1]) and (x in cluster[1]):
            izq_derecha = True

    if hacia_arriba and not izq_derecha:
        return 'hacia_arriba'
    elif not hacia_arriba and izq_derecha:
        return 'izq_derecha'
    elif hacia_arriba and izq_derecha:
        return 'ambas'
    else:
        return 0 # ninguna percolacion encontrada

def funcion_p(p):
    # funcion de probabilidad para sistemas de percolacion de 2x2
    return math.pow(p, 2) * (2 - math.pow(p, 2))

L = 2
p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
iteraciones = 1000
c = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for pi in range(len(p)): # iteracion para cada una de las probabilidades listadas en p
    print("Calculo de probabilidad de percolacion : ", p[pi])
    for it in range (iteraciones): # iteraciones para cada una de las probabilidades
        matriz = genera_matriz(L, L, p[pi]) 
        coords, indices = encuentra_clusters(matriz)
        percolate = existe_percolacion(coords, indices, L, L)        
        if (percolate!=0): # si existe alguna percolacion
            c[pi]+=1
    
    calculo_funcion = funcion_p(p[pi]) * 100 # calcula directamente probabilidad
    calculo_iteraciones = 100 - ((c[pi]/iteraciones)*100) # calcula del valor de percolaciones encontradas
    print("Probabilidad segun funcion: ", calculo_funcion)
    print("Probabilidad segun iteraciones: ", calculo_iteraciones)
    print("---------------\n")