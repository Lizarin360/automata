import pyautogui as robot
import time
import position
# Obtener el tamaño de la pantalla
# ancho_pantalla, alto_pantalla = pyautogui.size()
# srceenshot = robot.screenshot()
# robot.doubleClick(1700,500,1,"right",1);
# print(f"largo => {srceenshot.width} :: alto => {srceenshot.height} ::")
gps = position.Generales()

gps.obtPosicion()
gps.moverPosicion()

# Tiempo de espera entre movimientos
# espera = 3

# Mover a la esquina superior izquierda
# pyautogui.moveTo(0, 0, duration=espera)

# Mover a la esquina superior derecha
# pyautogui.moveTo(ancho_pantalla, 0, duration=espera)

# Mover a la esquina inferior derecha
# pyautogui.moveTo(ancho_pantalla, alto_pantalla, duration=espera)

# Mover a la esquina inferior izquierda
# pyautogui.moveTo(0, alto_pantalla, duration=espera)
