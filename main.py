
def main():
    txt = open('mapa_3.txt', 'r')
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
    start = []

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
                    start.append(tempS)
                temp.append(j)
                contTemp+=1
        mapa.append(temp)

    if contD != contO:
        print("Error. Las cargas o las bodegas")
        exit()

if __name__ == '__main__':
    main()
