#Crear un diccionario llamado informacion personal

información_personal = {
      "nombre" : "<Josselyn Luna>",
      "edad" : "18",
      "ciudad" : "Cañar",
      "Profesión" : "Docente"
  }
print(información_personal["nombre"])
print(información_personal["edad"])

  #Accede al valor asociado  con la clave "ciudad" y modifícalo con una ciudad diferente.
print(f"ciudad actual: {información_personal['ciudad']} ")
información_personal['ciudad']= "Cuenca"
print(f"Ciudad modificada: {información_personal['ciudad']}")


  #Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona.
información_personal['Profesión'] = "Ingeniera en TICS"
print(f"Profesión:{información_personal['Profesión']}")

#Verifica si la clave "telefono" existe en el diccionario.
#Si no existe, agrégala con un número de teléfono ficticio.
if "Teléfono" not in información_personal:
    información_personal['Teléfono'] = "0969832461"
    print("La clave 'telefono' no existía, se ha agregado.")
else:
    print("La clave Teléfono ya existe")

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
if "edad" in información_personal:
    del información_personal['edad']
    print("La clave 'edad' ha sido eliminada.")
else:
    print("La clave 'edad' no existe en el diccionario.")

# Imprimir el Diccionario Final
print("\nDiccionario actualizado:", información_personal)
