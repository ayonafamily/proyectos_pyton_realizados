#from pantalla import clear_screen

def main():
      """Calculo del factorial de un numero
            empleando recursión e iteración"""

      def numero():
            #Manejo de excepciones
            try:
                n = int(input("Ingrese número entero positivo a calcular: "))  
                #el factorial solo admite enteros               
                if n < 0: 
                    return None #retorna none cuando espera otro valor              
                    print("Sólo ingrese números positivos >= 0")
                else:
                    return n #si todo va bien, regresa el valor válido ingresado         
            except ValueError: #ingreso de cadenas
                print("Error en ingreso")        
                return None

      #Iteración
      def calcular_factorial(n):
           result = 1
           for i in range(n,0,-1):
               result = result * i        
           return(result)

      #Recursión
      def factorial(n):
              if n == 0:
                  return 1
              else:
                  return n * factorial(n-1)


      #########################################################################
      #Área de ejecución 

      #clear_screen()

      number = numero()


      print(f"Método de recursión: El factorial de {number} es: {factorial(number)}")

      print(f"Método de iteración: El factorial de {number} es: {calcular_factorial(number)}")

main()     
