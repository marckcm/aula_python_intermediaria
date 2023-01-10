"""
pyautogui.click
usa o pyautogui.position para saber a posição do x e do y e clicks para saber quantas vezeses sera clicado
pyautogui.write
escreve um texto informado em aspas
pyautogui.hotkey
teclas de atalho que podem ser executadas
pyautogui.press
pressiona a tecla selecionada enter tab etc
pyautogui.alert
cria um alerta e depois executa as funções
pyaytogui.PAUSE
de tempo em tempo o pyautogui executa a tarefa seguinte
pyautogui.position
com o print() mostra a posição do mouse na tela para usar no pyautogui.click
"""
import pyautogui
import pyperclip
import time

pyautogui.alert('VAI COMEÇAR A\n AUTOMAÇÃO APERTE OK')
pyautogui.hotkey('win', 'r')
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)
link = 'www.gmail.com'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=721, y=399, clicks=3)
# Se o e-mail for atualizado o position tem que ser renovado
time.sleep(7)
print(pyautogui.position())
