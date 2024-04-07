'''
Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas,
los guarde en una lista y muestre por pantalla su media y desviación típica.
'''
import numpy as np

def ingreso_datos():
    muestra_numeros = []
    while True:
        try:
            x = float(input("Ingrese números de la muestra: "))
            muestra_numeros.append(x)
        except ValueError:
            print("Ingrese solo números")
            continue
        continuar_agregando = input("¿Sigue agregando? (s/n): ").lower()
        if continuar_agregando == "n":
            return muestra_numeros # en vez de break

def medidas(muestra_numeros):
    if not muestra_numeros: # previene por si no se han ingresado numeros
        print("No se han ingresado números.")
        return
    print(f"La media es: {round(np.mean(muestra_numeros), 2)}")
    print(f"La desviación estándar es: {round(np.std(muestra_numeros), 2)}")
    print(f"el rango es: {max(muestra_numeros) - min(muestra_numeros)}")
    

muestra_numeros = ingreso_datos() # para que se procesen
print("\n")
medidas(muestra_numeros)
print("\n")

if __name__ == "__main__":
    print("el programa se ejecuta aquí")
else:
    print("El programa es parte de un módulo")




