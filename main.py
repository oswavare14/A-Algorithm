import sys
import math
import time

class Nodo():

    def __init__(self, padre=None, pos=None):
        self.padre = padre
        self.pos = pos

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos

def pCamino(end, tempM, camino,k):
    # hace el camino devuelta y retorna el camino para llegar al destino
    i,j = end
    while k > 1:
        if i > 0 and tempM[i - 1][j] == k - 1:
            i, j = i - 1, j
            camino.append((i, j))
            k -= 1
        elif j > 0 and tempM[i][j - 1] == k - 1:
            i, j = i, j - 1
            camino.append((i, j))
            k -= 1
        elif i < len(tempM) - 1 and tempM[i + 1][j] == k - 1:
            i, j = i + 1, j
            camino.append((i, j))
            k -= 1
        elif j < len(tempM[i]) - 1 and tempM[i][j + 1] == k - 1:
            i, j = i, j + 1
            camino.append((i, j))
            k -= 1
    return camino

def bfs(mapa,temp,char,cont):
    # se mueve en la matriz temporal haciendo los movimientos validos
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == cont:
                # revisa si el movimiento es valido y que pueda pasar por ese camino
                if (i > 0 and temp[i - 1][j] == 0 and mapa[i - 1][j] == '-') \
                        or (i > 0 and temp[i - 1][j] == 0 and mapa[i - 1][j] == 'D') \
                        or (i > 0 and temp[i - 1][j] == 0 and mapa[i - 1][j] == 'O') \
                        or (i > 0 and temp[i - 1][j] == 0 and mapa[i - 1][j] == char):
                    temp[i - 1][j] = cont + 1
                if (j > 0 and temp[i][j - 1] == 0 and mapa[i][j - 1] == '-') \
                        or (j > 0 and temp[i][j - 1] == 0 and mapa[i][j - 1] == 'D') \
                        or (j > 0 and temp[i][j - 1] == 0 and mapa[i][j - 1] == 'O') \
                        or (j > 0 and temp[i][j - 1] == 0 and mapa[i][j - 1] == char):
                    temp[i][j - 1] = cont + 1
                if (i < len(temp) - 1 and temp[i + 1][j] == 0 and mapa[i + 1][j] == '-') \
                        or (i < len(temp) - 1 and temp[i + 1][j] == 0 and mapa[i + 1][j] == 'D') \
                        or (i < len(temp) - 1 and temp[i + 1][j] == 0 and mapa[i + 1][j] == 'O') \
                        or (i < len(temp) - 1 and temp[i + 1][j] == 0 and mapa[i + 1][j] == char):
                    temp[i + 1][j] = cont + 1
                if (j < len(temp[i]) - 1 and temp[i][j + 1] == 0 and mapa[i][j + 1] == '-') \
                        or (j < len(temp[i]) - 1 and temp[i][j + 1] == 0 and mapa[i][j + 1] == 'D') \
                        or (j < len(temp[i]) - 1 and temp[i][j + 1] == 0 and mapa[i][j + 1] == 'O') \
                        or (j < len(temp[i]) - 1 and temp[i][j + 1] == 0 and mapa[i][j + 1] == char):
                    temp[i][j + 1] = cont + 1
    return temp

def astar(mapa, start, end):
    raiz = Nodo(None, start)
    raiz.g = raiz.h = raiz.f = 0
    final = Nodo(None, end)
    final.g = final.h = final.f = 0
    lista_A = []
    lista_B = []
    lista_A.append(raiz)
    cont1=0
    cont2=0

    # un while hasta que la lista quede vacia y no tenga mas nodos que revisar
    while len(lista_A) > 0:
        if len(lista_A) > 3000:
            print("A* Fallo" , "\n")
            break
        nodo_actual = lista_A[0]
        cont1 += 1
        index_actual = 0
        for index, item in enumerate(lista_A):
            if item.f < nodo_actual.f:
                nodo_actual = item
                index_actual = index

        lista_A.pop(index_actual)
        lista_B.append(nodo_actual)

        # Encontrando el Final
        if nodo_actual == final:
            camino = []
            c = nodo_actual
            while c is not None:
                camino.append(c.pos)
                c = c.padre
            print("Total de nodos explorados: ",cont2 )
            print("Total de nodos descubiertos: ", cont1)
            return camino[::-1] # retorna el camino

        # hace un hijo y agrega su posicion
        hijo = []
        for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            cont2 += 1
            pos_nodo = (nodo_actual.pos[0] + k[0], nodo_actual.pos[1] + k[1])
            # Posicion sea dentro del mapa, una posicion valida
            if pos_nodo[0] > (len(mapa) - 1) or pos_nodo[0] < 0 or pos_nodo[1] > (len(mapa[len(mapa)-1]) -1) or pos_nodo[1] < 0:
                continue
            # Pueda caminar en el mapa
            if mapa[pos_nodo[0]][pos_nodo[1]] != '-' and mapa[pos_nodo[0]][pos_nodo[1]] != 'D' and mapa[pos_nodo[0]][pos_nodo[1]] != '<'\
                    and mapa[pos_nodo[0]][pos_nodo[1]] != '>' and mapa[pos_nodo[0]][pos_nodo[1]] != '^' and mapa[pos_nodo[0]][pos_nodo[1]] != 'v':
                continue
            nuevo = Nodo(nodo_actual, pos_nodo)
            hijo.append(nuevo)

        # revisa cada hijo de la lista
        for i in hijo:
            for closed_child in lista_B:
                if i == closed_child:
                    continue
            # Calculo del heuristico
            i.g = nodo_actual.g + 1
            i.h = ((i.pos[0] - final.pos[0]) ** 2) + ((i.pos[1] - final.pos[1]) ** 2)
            i.f = i.g + i.h
            for j in lista_A:
                if i == j and i.g > j.g:
                    continue
            lista_A.append(i)

#funcion lee el mapa
def leer_mapa():
    txt = open(sys.argv[1], 'r')
    return txt

#ordena unas tuplas de listas
def ordenar(camino):
    temp= []
    for j in reversed(camino):
        temp.append(j)
    return temp

def main():
    # Se lee lo que se manda desde consola
    txt = leer_mapa()
    tamaño = txt.readline()
    columnas = ""
    filas = ""
    bandera = True;

    #toma el tamaño de la matriz
    for i in tamaño:
        if i != ',':
            if bandera:
                filas += i
            else:
                columnas += i
        else:
            bandera = False


    filas = int(filas)
    columnas = int(columnas)
    contO = 0
    contD = 0
    mapa = []
    positionD = []
    positionO = []
    positionD2 = []
    positionO2 = []
    inicio = []
    tempChar = ''

    # camptura todas las posiciones de carga, descarga y guarda otra informacion
    for i in range(0,filas):
        temp = []
        contTemp = 0
        for j in txt.readline():
            if j != '\n':
                if j == 'D':
                    contD += 1
                    tempD = []
                    tempD.append(i)
                    tempD.append(contTemp)
                    positionD.append(tempD)
                if j == 'O':
                    contO += 1
                    tempO = []
                    tempO.append(i)
                    tempO.append(contTemp)
                    positionO.append(tempO)
                if j == '>' or j == '^' or j == '<' or j == 'v':
                    tempChar = j
                    tempS = []
                    tempS.append(i)
                    tempS.append(contTemp)
                    inicio.append(tempS)
                temp.append(j)
                contTemp+=1
        mapa.append(temp)

    # el menu del programa
    bandera2 = True
    CaminoBFS = []
    CaminoAS = []
    totalCamino = contD * 2
    nuevoInicio = 0,0
    positionD2 = positionD
    positionO2 = positionO

    while bandera2:
        print("1 - BFS")
        print("2 - A*")
        print("3 - Salir")

        x = int(input())
        print()
        if x == 1:
            Tiempo1 = time.time()

            for l in range(totalCamino):
                # crea un matriz temporal que marca el camino
                tempM = []
                for i in range(len(mapa)):
                    tempM.append([])
                    for j in range(len(mapa[i])):
                        tempM[-1].append(0)

                start = 0,0
                end = 0,0
                if l == 0:
                    start = (inicio[0][0], inicio[0][1])
                    end = (positionD[0][0],positionD[0][1])
                else:
                    if l % 2 != 0:
                        start = nuevoInicio
                        end = (positionO[0][0], positionO[0][0])
                        positionO.pop(0)
                    elif l % 2 == 0:
                        start = nuevoInicio
                        end = (positionD[0][0], positionD[0][0])
                        positionD.pop(0)
                i, j = start
                tempM[i][j] = 1
                c = 0
                # manda a llamar la funcion bfs que hace el recorido y devuelve el camino en la matriz temporal
                while tempM[end[0]][end[1]] == 0:
                    c += 1
                    tempM = bfs(mapa, tempM, tempChar, c)

                i, j = end
                k = tempM[i][j]
                camino = [(i, j)]
                # agrega el recorido al recorido completo
                recorido = pCamino(end, tempM, camino, k)
                recorido.pop(0)
                ordenar(recorido)
                nuevoInicio = (recorido[0][0],recorido[0][1])
                recorido2 = ordenar(recorido)
                CaminoBFS.append(recorido2)
            print(CaminoBFS, '\n')
            Tiempo2 = time.time()
            print("Total de nodos explorados: ",c)
            print("Total de nodos descubiertos: ",k)
            print("El BFS tomo un tiempo de: ", Tiempo2 - Tiempo1, "\n")
        elif x == 2:
            Tiempo1 = time.time()
            for l in range(totalCamino):
                start = 0, 0
                end = 0, 0
                if l == 0:
                    start = (inicio[0][0], inicio[0][1])
                    end = (positionD2[0][0], positionD2[0][1])
                else:
                    if l % 2 != 0:
                        start = nuevoInicio
                        end = (positionO2[0][0], positionO2[0][0])
                        positionO2.pop(0)
                    elif l % 2 == 0:
                        start = nuevoInicio
                        end = (positionD2[0][0], positionD2[0][0])
                        positionD2.pop(0)

                path = astar(mapa, start, end)
                CaminoAS.append(path)
            Tiempo2 = time.time()
            print("El A* tomo un tiempo de: ", Tiempo2 - Tiempo1,"\n")

        elif x == 3:
            bandera2 = False
        else:
            print("Comando invalido" , "\n")

    if contD != contO:
        print("Error. Las cargas o las bodegas \n")
        exit()

if __name__ == '__main__':
    main()
