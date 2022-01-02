import time;
from Tablero import *;
from Jugada import *;

for i in range(9):
    if i > 9:
        break

    Jugada[(i)]= "X"

    time.sleep(2)

    Tablero(Jugada)
