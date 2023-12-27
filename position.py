import pyautogui as rob
class Generales:
    position=[]
    def __init__(self):
        return

    def obtPosicion(self):
        posicion = rob.position()
        print(posicion)

    def moverPosicion(self):
        rob.moveTo(2900,21,1)
        rob.moveTo(5714,35,1)
        rob.moveTo(2937,1469,1)
        rob.moveTo(5724,1481,1)




# Gps = Generales()