def tienda():
    stock_manzanas = 20
    precio_manzanas = 5.0

    print("==============================")
    print("==      Bienvenido a la     ==")
    print("==    Tienda De Manzanas    ==")
    print("==============================")

    nombre_usuario = input("Ingresa tu nombre:  " )    
    apellido_usuario = input("Ingresa tu apellido: ")
    print("Bienvenido", nombre_usuario, apellido_usuario)
    print("Al momento contamos con", stock_manzanas, "manzanas para la venta a S/.", precio_manzanas,"la unidad")
    print("¿Cuántas quieres llevar?")

    manzanas_pedido = int(input())
    total_manzanas = manzanas_pedido * precio_manzanas

    print("Compraste", manzanas_pedido,"manzanas. El total a pagar es: S/.", total_manzanas)
    print("te quedan", stock_manzanas - manzanas_pedido,"a tu disposicion")
    print("Gracias por tu compra. \nVuelve pronto!!.")
    
tienda()