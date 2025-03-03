#crear una matriz
matriz = [
    [6, 3, 8 ],
    [4, 5, 7 ],
    [3, 2, 9 ]
]
#funcion para ordenar una fila de manera ascendente usanso Bubble Sort

def bubble_sort_fila(fila):
    n=len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

#funcion para mostrar la matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

#mostrar la matriz original
print ("Matriz Original:")



