import funciones as f   
jugadores = []
while True:
    print("1.- Registrar puntajes Torneo")
    print("2.- Listar todos los puntajes" )   
    print("3.- Imprimir por tipo ")
    print("4.- Salir del programa" ) 
    try:
        opc = int(input("Ingrese un opcion: ")) 
        if opc == 1:
            f.registrar(jugadores)
        elif opc== 2:
            f. mostar(jugadores)
        elif opc ==3:
            f.imprimir(jugadores)
        elif opc == 4:
           print("Saliendo.....")
           break
        else:
          print("Ingrse una opcion valida")
    except:
        print("Ingrese un numero")



