from pantalla import clear_screen

def main():
    """Función principal"""
    numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    palo = ["t", "o", "c", "p"]

    def barajar(numero, palo):
        baraja: list = [n + p for n in numero for p in palo]
        return baraja
    
    clear_screen() #alimpia pantalla
    
    baraja = barajar(numero, palo)
    print(f'Resultado :{baraja}')
    

    

main()











        
        
