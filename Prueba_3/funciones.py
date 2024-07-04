juegos = [ "fortnite","valorant","fifa"]
tipos = ["principiante" ,"avanzado", "experto"]  
def registrar(datos):
    Id= input("ingrese id del jugador: ")
    nombre= input("ingrese nombre del jugador y apellido: ")
    juego=input("Ingrese el juego que juega (fortnite/valorant/fifa: ").lower()
    if juego in juegos:
        try:
            puntos= int(input("Ingrese los puntos obtenidos: "))
            if puntos> 0:
                tipo =input("Ingrese su tipo (Principiante/Avanzado/Experto): ").lower()
                if tipo in tipos:
                    datos.append ({
                        "Id Jugador" : Id,
                        "Nombre" : nombre,
                        "Juego": juego,
                        "Puntos" : puntos,
                        "Tipo": tipo
                        })
                else: 
                    print("Ingrese un tipo de jugador valido")
            else: 
                print("Puntos invalidos")
        except:
            print("Ingrese un numero")


def mostar(datos):
      for diccionario in datos:
          for clave, valor in diccionario.items():
              print(f"{clave} {valor}\n")



def imprimir(datos):
    tipo = input("Ingrese un tipo de jugador (Principiante/Avanzado/Experto): ").lower()
    encontrado = False
    if tipo in tipos:
        for clave in datos:
            if clave["Tipo"].lower() == tipo:
             encontrado = True
             print(clave)
             archivo = clave 
             with open ("archivo.txt", "w") as archivo:
                 for clave in datos:
                     archivo.write(f"{clave} \n")
    if not encontrado:
        print("Ese tipo de jugador no esta")    

 
