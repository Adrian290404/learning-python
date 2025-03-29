import pyautogui
import time
import keyboard

print("Autoclicker iniciado. Presiona SPACE para detenerlo.")

while True:
    if keyboard.is_pressed('space'):
        print("Autoclicker detenido.")
        break
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    pyautogui.click(center_x, center_y)
    time.sleep(80)
