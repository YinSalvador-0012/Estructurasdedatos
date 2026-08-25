print("3 Ejemplos de listas con diferentes métodos") 
lista = ["Jean", "Carlos", "Salvador"]
lista.append("Garza")
print(lista)
print("--------------------------------------------------------------------------------")


lista.pop(3)
print(lista)

print("----------------------------------------------------------------------------------")

lista.extend(["Garza","Rios"])
print(lista)

print("------------------------------------------------------------------------------------")
print("")

print("3 EJEMPLOS DE TUPLAS CON DIFERENTES METODOS ")
tupla= (10,100, 1000)
print(tupla)
print(tupla.count(100))
print(tupla.index(100))

print("------------------------------------------------------------------------------------")
print("")

print("3 EJEMPLOS DE DICCIONARIOS") 
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

print("---------------------------------------------------------------------------------")

print("3 EJEMPLOS DE CONJUNTOS")
print("")
print("1er EJEMPLO DE CONJUNTOS .copy()") 
conjunto=set([1,2,3,4])

conjunto_copia=conjunto.copy()
print(conjunto)
print(conjunto_copia)

print("")
print("2do EJEMPLO DE CONJUNTOS .add()")
print(conjunto_copia)
conjunto_copia.add(5) 
print(conjunto_copia)

print("")
print("3er EJEMPLO DE CONJUNTOS .clear()")
conjunto_copia.clear()
print(conjunto) 
print(conjunto_copia)