# Author CabaCrD
#JUEGO QUE CONSISTE EN LA RULETA RUSA, DE FORMA ALEATORIA SE GENERARAN DOS NUMEROS, SI ESTOS COINCIDEN PERDERAS LA PARTIDA

import random #IMPORTAMOS RANDOM

aleatorio = random.randint(1, 6) #NUMERO ALEATORIO DE LA IA
aleatorioJugador = random.randint(1, 6) #NUMERO ALEATORIO DEL JUGADOR

#MENSAJES DE BIENVENIDA
print("Bienvenido")
print("Este es un juego de vida o muerte. Si eliges mal, perderás tus datos.")

while True: #BUCLE WHILE

    try: #MANEJO DE EXCEPCIONES

        disparo = input("¿Vas a apretar el gatillo?(S/N)").upper() #NOS PREGUNTARA SI QUEREMOS APRETAR EL GATILLO

        if disparo =="S": #SI SE PULSA EL BOTON S

            break #ROMPEREMOS EL BUCLE

        if disparo =="N": #SI SE PULSA EL BOTON N

            print("Parece que te has rendido, pues nada, vamos a cerrar el programa") #MENSAJE DE DESPEDIDA
            quit() #CERRAMOS EL PROGRAMA
            
        else: # SI SELECCIONAMOS UNA OPCION INVALIDA

            print("Por favor, elija S O N")

    except ValueError:

        print("Por favor, ingrese un opción válida.")

if aleatorioJugador == aleatorio: #SI LOS DOS ALEATORIOS COINCIDEN

    print("Has PERDIDO") 

else: #SI NO LLEGAN A A COINCIDIR

    print("¡Has GANADO!")
