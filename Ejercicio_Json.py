import json

# 1. Creamos un diccionario normal de Python con datos de prueba
mi_perfil = {
    "nombre": "Jean Carlos ",
    "edad": 21,
    "estudiante": True,
    "gustos": ["Programar", "Música"]
}

# 2. GUARDAR: Convertir el diccionario y guardarlo en un archivo JSON
# Usamos open() en modo escritura ("w" = write)
with open("perfil.json", "w", encoding="utf-8") as archivo:
    json.dump(mi_perfil, archivo, indent=4, ensure_ascii=False)

print("¡Los datos se guardaron en 'perfil.json'!")


# 3. LEER: Abrir el archivo JSON y traer los datos de vuelta a Python
# Usamos open() en modo lectura ("r" = read)
with open("perfil.json", "r", encoding="utf-8") as archivo:
    datos_recuperados = json.load(archivo)

print("\n--- DATOS LEÍDOS DEL ARCHIVO ---")
print(datos_recuperados)

# Podemos usar los datos como cualquier diccionario
print(f"\nHola, me llamo {datos_recuperados['nombre']} y tengo {datos_recuperados['edad']} años.")