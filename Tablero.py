# Juego de Tic-Tac-Toe
from os import system
from saludo import *;
from Jugada import *;
from saludo import *;



T="""
          +-+-+-+-+-+-+-+
          |T|a|b|l|e|r|o|
          +-+-+-+-+-+-+-+
""";



#Defino el tablero

def Tablero(Jugada):
    system("cls")
    return (print(f"""{T}
          a      b      c   
       ______________________
       |      |      |      |
  1    |  {Jugada[0]}   |  {Jugada[1]}   |  {Jugada[2]}   |
       |      |      |      |
       |------|------|------|
       |      |      |      |
  2    |  {Jugada[3]}   |  {Jugada[4]}   |  {Jugada[5]}   |
       |      |      |      |
       |------|------|------|
       |      |      |      |
  3    |  {Jugada[6]}   |  {Jugada[7]}   |  {Jugada[8]}   |
       |      |      |      |
       ----------------------
    Jugador = {Jugador1}   
    Jugador = {Jugador2}   """))
  
  
