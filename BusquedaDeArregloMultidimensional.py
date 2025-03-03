#defino una matriz
matriz = [
  [1, 2, 3 ],
  [4, 5, 6 ],
  [7, 8, 9 ]

]

def buscar_valor(matriz,valor):
    # recorrer y buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i,j # retorna la posicion
    return None

#solicito el valor a buscar
numero_buscar=6

#llamo a la funcion
resultado = buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"resultado del numero {numero_buscar} se encuentra en la posicion  {resultado[0]}{resultado[1]}")
else:
    print(f"No se encontro el numero ")






