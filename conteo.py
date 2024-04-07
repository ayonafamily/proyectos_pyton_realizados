'''
Programa que cuenta el número de visitantes del Hotel libertador
según nacionalidad. 

'''
from pantalla import clear_screen, salto_linea
from collections import Counter

libertador_casos = [
    "Chilena","Chilena","Chilena","Chilena",
    "Chilena","Argentina","Argentina","Argentina",
    "Argentina","Argentina","Argentina","Argentina",
    "Argentina","Argentina","Argentina","Argentina","Boliviana",
    "Boliviana","Boliviana","Boliviana","Boliviana",
    "Boliviana","Boliviana","Boliviana","Boliviana","Brasileña",
    "Brasileña","Brasileña","Brasileña","Brasileña",
    "Chilena","Chilena","Chilena","Chilena","Chilena",
    "Argentina","Argentina","Argentina",
    "Argentina","Argentina","Argentina","Argentina",
    "Argentina","Argentina","Argentina","Argentina","Boliviana",
    "Boliviana","Boliviana","Boliviana","Boliviana",
    "Boliviana","Boliviana","Boliviana","Boliviana","Brasileña",
    "Brasileña","Brasileña","Brasileña","Brasileña",
    "Chilena","Chilena","Chilena","Chilena","Chilena",
    "Argentina","Argentina","Argentina",
    "Argentina","Argentina","Argentina","Argentina",
    "Argentina","Argentina","Argentina","Argentina","Boliviana",
    "Boliviana","Boliviana","Boliviana","Boliviana",
    "Boliviana","Boliviana","Boliviana","Boliviana","Brasileña",
    "Brasileña","Brasileña","Brasileña","Brasileña"
]

clear_screen()

# Método fuerza bruta
# libertador_etiquetas = []
# # Lista para almacenar las primeras ocurrencias de cada nombrem

# vistos = set()

# # Recorrer la lista original
# for nombre in libertador_casos:    
#     # Si el nombre no está en el conjunto de nombres vistos, añadirlo a la lista de primeras ocurrencias y al conjunto de nombres vistos
#     if nombre not in vistos:
#         libertador_etiquetas.append(nombre)
#         vistos.add(nombre)
# print("")
# print("Hotel Libertador\nFrecuencias Simples por nacionalidad\n")
# def frecuencias_simples():
#     for x in libertador_etiquetas:    
#         if x in libertador_casos: # conteo de casos
#             casos = libertador_casos.count(x)
#             print("Hay ", casos,"huespedes", "de nacionalidad", x)        
#         else:
#             print("No se encuentra lo que busca")
#             break
#     print("Total casos examinados",(len(libertador_casos)))

# frecuencias_simples()     
print("")

salto_linea()

# Obtener las frecuencias utilizando Counter
frecuencias = Counter(libertador_casos)

print("\nHotel Libertador\nFrecuencias Simples por nacionalidad\n")

# Imprimir las frecuencias
for nacionalidad, cantidad in frecuencias.items():
    print(f"Hay {cantidad} huéspedes de nacionalidad {nacionalidad}")

print("\nTotal casos examinados:", len(libertador_casos), "\n")