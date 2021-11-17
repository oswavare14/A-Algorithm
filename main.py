class Nodo():

    def __init__(self, padre=None, pos=None):
        self.padre = padre
        self.pos = pos

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos


def astar(mapa, start, end):
    raiz = Nodo(None, start)
    raiz.g = raiz.h = raiz.f = 0
    final = Nodo(None, end)
    final.g = final.h = final.f = 0
    lista_A = []
    lista_B = []
    lista_A.append(raiz)

    while len(lista_A) > 0:
        nodo_actual = lista_A[0]
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
            return camino[::-1] # Return reversed path

        hijo = []
        for k in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            pos_nodo = (nodo_actual.pos[0] + k[0], nodo_actual.pos[1] + k[1])
            # Posicion sea dentro del mapa, una posicion valida
            if pos_nodo[0] > (len(mapa) - 1) or pos_nodo[0] < 0 or pos_nodo[1] > (len(mapa[len(mapa)-1]) -1) or pos_nodo[1] < 0:
                continue
            # Pueda caminar en el mapa
            if mapa[pos_nodo[0]][pos_nodo[1]] != '-':
                continue
            nuevo = Nodo(nodo_actual, pos_nodo)
            hijo.append(nuevo)

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

def main():
    txt = open('mapa_2.txt', 'r')
    tamaño = txt.readline()
    columnas = ""
    filas = ""
    bandera = True;

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
    inicio = []

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
                    tempS = []
                    tempS.append(i)
                    tempS.append(contTemp)
                    inicio.append(tempS)
                temp.append(j)
                contTemp+=1
        mapa.append(temp)

    t = (0,0)
    y = (3,4)
    path = astar(mapa, t, y)
    print(path)

    if contD != contO:
        print("Error. Las cargas o las bodegas")
        exit()

if __name__ == '__main__':
    main()
