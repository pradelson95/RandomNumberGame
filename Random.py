import random
from time import sleep

numerodejugador1 = random.randint(1,200)
numerodejugador2 = random.randint(1,200)

Nombredejugador1 = input("\033[92m Ingrese el nombre del jugador 1 por favor:")
sleep(2)

Nombredejugador2 = input("\033[95m Ingrese nombre del jugador 2 por favor:")
sleep(2)

jugador1 = input("\033[1m Escribe  la letra j para que tengas un numero del 1 al 40:")
sleep(2)

jugador2 = input("\033[1m Escribe la letra j para que tu tengas un numero del 1 al 40:")
sleep(2)

if numerodejugador1>numerodejugador2:
    print(f"\033[1m El ganador es {Nombredejugador1} porque su numero es el " + str(numerodejugador1) + " y el numero de su oponente es el {numerodejugador2}")
    sleep(2)

else:
    print(f"\033[91m El ganador es {Nombredejugador2} porque su numero es el " + str(numerodejugador2) + " y el numero de su oponente es el",numerodejugador1)
    sleep(2)