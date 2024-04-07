from pantalla import clear_screen
def main():
    #calificacion = 34
    clear_screen()    
    nota = ingreso_nota()
    status_alumno(nota)

    
    """Métodos"""
    
def ingreso_nota():
    try:
        calificacion = int(input("Ingrese las notas: "))            
        if calificacion >= 0 :
            return calificacion 
        elif calificacion != type(int) : #numerico, o vacío
            print("Imposible calificar")          

        else:
            print("nota inválida")
    except ValueError:
        print("Datos desconocidos")  
    
        
 
def status_alumno(calificacion):
    if calificacion >= 70 and calificacion < 100:
        print("Alumno Aprobado")
    elif calificacion > 100:
        print("Imposible. Calificacion máxima = 100")
    
    else:
        print("Alumno No aprobado")

if __name__ == '__main__':
    main()