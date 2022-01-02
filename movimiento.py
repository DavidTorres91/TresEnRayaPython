from Tablero import *;
from Jugada import *;
from saludo import *;
j1="";
j2=""

def movimiento():
    
    print(f"""{Jugador1}  cual es tu movimiento?""")
    print("Ejemplo a1")
    j1 = input()
    
    if j1 == "a1":
      if Jugada[0]!="." :
        Jugada[0]="X"
        Tablero(Jugada)
      else: ("Casilla Ocupada.")
      

        
    elif j1 == "b1":
        Jugada[1]="X"
        Tablero(Jugada)

        
    elif j1 == "c1":
        Jugada[2]="X"
        Tablero(Jugada)

        
    elif j1 == "a2":
        Jugada[3]="X"
        Tablero(Jugada)
        
    elif j1 == "b2":
        Jugada[4]="X"
        Tablero(Jugada)

        
    elif j1 == "c2":
        Jugada[5]="X"
        Tablero(Jugada)

        
    elif j1 == "a3":
        Jugada[6]="X"
        Tablero(Jugada)

        
    elif j1 == "b3":
        Jugada[7]="X"
        Tablero(Jugada)

        
    elif j1 == "c3":
        Jugada[8]="X"
        Tablero(Jugada)

        
    else:
        print("Por favor seleciones una opcion valida")
     

    print(f"""{Jugador2} cual es tu movimiento?""")
    print("Ejemplo a1")
    j2 = input()

    if j2 == "a1":
        Jugada[0]="O"
        Tablero(Jugada)

        
    elif j2 == "b1":
        Jugada[1]="O"
        Tablero(Jugada)

        
    elif j2 == "c1":
        Jugada[2]="O"
        Tablero(Jugada)

        
    elif j2 == "a2":
        Jugada[3]="X"
        
    elif j2 == "b2":
        Jugada[4]="O"
        Tablero(Jugada)

        
    elif j2 == "c2":
        Jugada[5]="O"
        Tablero(Jugada)

        
    elif j2 == "a3":
        Jugada[6]="O"
        Tablero(Jugada)

        
    elif j2 == "b3":
        Jugada[7]="O"
        Tablero(Jugada)

        
    elif j2 == "c3":
        Jugada[8]="O"
        Tablero(Jugada)

        
    else:
        print("Por favor seleciones una opcion valida")

        
    return movimiento()