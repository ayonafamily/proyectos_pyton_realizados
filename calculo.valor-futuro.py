def main():
    """Cálculo del valor futuro de uno
    monto, a cierta tasa, en un período"""
    
    p  = float(input("monto principal ")) # monto principal
    i  = float(input("tasa interés anual "))   #tasa de interes anual
    n  = float(input("tiempo en años "))

    def valor(p,i,n):
        FV = p * (1 + i/100)**n
        return FV
        
    resultado = valor(p,i,n)

    print("El valor futuro de ", p,"a ", i,"anual",n,"años es: ", resultado)

    valor(p,i,n)

main()
