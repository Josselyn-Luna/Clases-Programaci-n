#Crear una funcion llamada Calcular Descuento con dos parámetros:
#el monto total de la compra y un valor del descuento
#Calcular el descuento aplicando el porcentaje al valor total
#Devolver el monto del descuento calculado
def calcular_descuento(valor_total, porcentaje_descuento=20):
    descuento = valor_total * (porcentaje_descuento/100)
    return descuento

if __name__ == "__main__":
    valor1 = 1200
    valor2 = 2500
# llamo a la funcion
    descuento1 = calcular_descuento(valor1)
    print(f"El valor de tu compra es {valor1}, y el descuento es de {descuento1}")

#llamo a la funcion
    porcentaje_descuento= 70
    descuento2 = calcular_descuento(valor2)
print(f"El valor de tu compra es {valor2}, y el descuento es de {descuento2}")
