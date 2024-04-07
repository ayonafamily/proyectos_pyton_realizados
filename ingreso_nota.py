## from pantalla import clear_screen
def main():  
    # Ingreso del nombre del estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ").capitalize()

    # Llamada a los métodos
    notas, cantidad_notas = ingreso_notas()
    calculo_promedio(notas, cantidad_notas, nombre_estudiante)

def ingreso_notas():    
    """Método para ingresar las notas"""
    cantidad_notas = [1, 2, 3, 4, 5]
    notas = []      
    for i in cantidad_notas:
        nota = int(input(f"Ingrese nota {i}: "))
        notas.append(nota)
    return notas, cantidad_notas

def calculo_promedio(notas, cantidad_notas, nombre_estudiante):
    """Método para calcular el promedio"""
    promedio = sum(notas) / len(cantidad_notas)
    print(f"\nEl promedio de {nombre_estudiante} es: {promedio:.2f}")

# No edites estas dos líneas siguientes
# Indican a Python que ejecute la función principal
if __name__ == '__main__':
    main()
