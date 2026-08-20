#3 Ejemplos de listas con diferentes métodos 
lista = ["Jean", "Carlos", "Salvador"]
lista.append("Garza")
print(lista)
print("--------------------------------------------------------------")


lista.pop(3)
print(lista)

print("--------------------------------------------------------------")

lista.extend(["Garza","Rios"])
print(lista)

#3 EJEMPLOS DE TUPLAS CON DIFERENTES METODOS 
tupla= (10,100, 1000)
print(tupla)



#3 EJEMPLOS DE DICCIONARIOS 
diccionario = {"a":1, "b":2, "c":3}
v_items = diccionario.items()
print(v_items)

#2do ejemplo con keys 
diccionario = {"a":1, "b":2, "c":3}
v_keys = diccionario.keys()
print(v_keys)

#3er ejemplo con valores 
diccionario = {"a":1, "b":2, "c":3}
v_valores = diccionario.values()
print(v_valores)
