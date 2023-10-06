import numpy as np
import random


#Implementacion de la funcion de localidad
def N(instance:list, type=0) -> list:
    neighborhood = []
    n = np.size(instance)
    for i in range(n):
        for j in range(n):
            if (j==i):
                continue
            #Tipo de vecindad generada
            if (type==0):
                neighbor = insert(instance, i, j)
            elif (type==1):
                neighbor = swap(instance, i, j)
            neighborhood.append(neighbor)
    return np.unique(neighborhood, axis=0)

def insert(instance:list, index_i:int, index_j:int) -> list:
    return np.insert(np.delete(instance, index_i), index_j, instance[index_i]).tolist()

def swap(instance:list, index_i:int, index_j:int) -> list:
    temp = np.copy(instance)
    temp[index_i] = instance[index_j]
    temp[index_j] = instance[index_i]
    return temp


def show_neighborhood(neighborhood:list) -> int:
    print("VECINDAD con {} elementos".format(len(neighborhood)))
    id=1
    for i in neighborhood:
        print("{} : {}".format(id, i))
        id+=1
    return

#--------------------------------------------------------------------------------
# Leemos datos del problema desde fichero

def read_instance_QAP(filepath : str) -> list:
    lines = open(filepath).readlines()
    # Leemos cabecera
    n = int(lines[0].strip().split()[0])

    # Leemos D_ij
    D = [line.split() for line in lines[1:n+1]]
    D = np.array(D, dtype=float)

    # Leemos H_ij
    H = [line.split() for line in lines[n+1:]]
    H = np.array(H, dtype=float)

    return (n, D, H)

# Definimos función objetivo para evaluar candidatos
def objective_function_QAP(solution : list, instance : list) -> list:
    n, D, H = instance

    fitness = 0
    for i in range(n):
        for j in range(n):
            fitness += D[i][j] * H[solution[i]][solution[j]]
    return fitness

#--------------------------------------------------------------------------------
#Selecciona un vecino por BEST_FIRST-0, GREDDY-1 o RANDOM-2
def analizaVecindad(current: list, fitness: float, opcion: int) -> (float, list, bool):
    #Obtenemos la vecindad del current
    vecindad=N(current, 0)
    #show_neighborhood(vecindad)
    #print("Tamaño de vecindad: {}".format(len(vecindad)))
    
    #BEST_FIRST
    if (opcion==0):
        vecino=vecindad[random.randint(0,len(vecindad)-1)]
        #print(vecino)
        #Obtenemos su valor fitness
        fitness_n=objective_function_QAP(vecino,instance)
        #print(fitness_n)
        #Comparamos el current con el vecino: Si no es mejor, regresamos current
        print("Current: {} - Vecino: {}".format(current, vecino))
        if(VecinoMejor(fitness,fitness_n)):
            print("EL VECINO ES MEJOR")
            return (fitness_n,vecino,True)
        else:
            print("EL CURRENT ES MEJOR")
            return (fitness,current,False)
        
    #GREEDY
    elif (opcion==1):
        #Inicializamos nuevo current
        new_current=current
        new_fitness=fitness
        for i in range(len(vecindad)):
            #Obtenemos valores fitness para cada vecino
            fitness_n=objective_function_QAP(vecindad[i],instance)
            #print("Fitness del vecino {}:  {}".format(i,fitness_n))
            if(fitness_n<new_fitness):
                new_current=vecindad[i]
                new_fitness=fitness_n
                #print("cambio")
        
        if(VecinoMejor(fitness,new_fitness)):
            print("EL VECINO ES MEJOR")
            return (new_fitness,new_current,True)
        else:
            print("EL CURRENT ES MEJOR")
            return (fitness,current,False)
        
    #RANDOM
    elif (opcion==2):
        vecino=vecindad[random.randint(0,len(vecindad)-1)]
        fitness_n=objective_function_QAP(vecino,instance)
        if(VecinoMejor(fitness,fitness_n)):
            print("EL VECINO ES MEJOR")
            return (fitness_n,vecino,True)
        else:
            print("EL CURRENT ES MEJOR")
            return (fitness,current,False)


#Determina si el vecino es mejor que el current
def VecinoMejor(fitness_current:float, fitness_n:float) -> bool:
    return True if fitness_n < fitness_current else False
#--------------------------------------------------------------------------------
def local_search(instance : list, max_evals : int) -> list:
    '''
    :param instance: instancia del problema
    :param max_evals: numero maximo de iteraciones a realizar
    :return: solucion, fitness del candidato y número de evaluaciones
    '''

    # TODO
    # Generamos un primer candidato naive y calculamos fitness
    size = instance[0]
    candidate = np.random.permutation(list(range(size)))
    fitness = objective_function_QAP(candidate, instance)

    mejora = True
    n_evals = 1

    ## TODO (APROX 20 LINEAS)

    while (mejora==True and n_evals<=max_evals):
        (best_fitness, best_candidate, mejora)=analizaVecindad(candidate,fitness,1)
        print("Current: {} - Vecino: {}".format(candidate, best_candidate))
        print("Fitness_Current: {} - Fitness_Vecino: {}".format(fitness, best_fitness))
        if(mejora==True):
            print("NUEVO CANDIDATO")
            candidate=best_candidate
            fitness=best_fitness

        n_evals+=1

    return (best_fitness, best_candidate, n_evals)
#--------------------------------------------------------------------------------



# Cargamos instancia
instance = read_instance_QAP("tai20a.dat")

# Explora la vecindad de nuestro candidato para analizar si podemos mejorar la solución inicial
(best_fitness, best_solution, n_evals) = local_search(instance, 10)
print("Best fitness: {} - best candidate: {} - No evaluaciones: {}".format(best_fitness, best_solution, n_evals)) 




