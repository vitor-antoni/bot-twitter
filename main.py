# @vitor-antoni

import pyautogui, time

print("\nO bot está sendo iniciado.", end="")

for c in range(0, 4):
    time.sleep(0.5)
    print(".", end="", flush=True)

mensagem = str(input("\nO que voce deseja twittar? "))

time.sleep(2)

# Abre o Navegador
pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("Opera")        # Altere para o nome do seu navegor
pyautogui.press("enter")

time.sleep(3)

# Digita o link do site
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://twitter.com/home")
pyautogui.press("enter")

time.sleep(4)

# Digita mensagem
pyautogui.moveTo(715, 185, duration=0)
    # Altere se utilizar resolução diferente de 1920x1080
    # Verifique as coordenadas do mouse no projeto testeCursorMouse.py
    
pyautogui.leftClick()
pyautogui.write(mensagem)

time.sleep(3)

# Twitta
pyautogui.moveTo(1150, 282, duration=0)
pyautogui.leftClick()

print("O bot fez o trabalho dele! :D")