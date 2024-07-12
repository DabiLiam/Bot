import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

# Abrir o navegador
pyautogui.press('win')
pyautogui.write('chorome')
pyautogui.press('enter')
pyautogui.moveTo(x=699, y=686)
pyautogui.click()

# Entrar na shopee
pyautogui.write('https://shopee.com.br/seller/login')
pyautogui.press('enter')

time.sleep(3)

# Fazer o Loguin
pyautogui.click(x=1236, y=404)
pyautogui.write('Seu Email....')
pyautogui.press('tab')
pyautogui.write('Sua senha...')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

# Ir até area de pedidos concluidos
pyautogui.click(x=1562, y=112)
pyautogui.click(x=1469, y=211)

time.sleep(3)

pyautogui.click(x=697, y=265)

# Base de dados
tabela = pandas.read_csv('Seu banco de dados...')

print(tabela)

time.sleep(3)

# Execução da tarefa
def downloads_ID(linha):
    pyautogui.click(x=819, y=341)
    pyautogui.hotkey('ctrl', 'a')
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('enter')
    pyautogui.click(x=1650, y=540)
    pyautogui.click(x=1661, y=612)
    
numero_de_repeticoes = 5


# Loop para repetir o processo da tarefa
for linha in range(numero_de_repeticoes):
    y = downloads_ID(linha)

input("Pressione Enter para encerrar o script e fechar o navegador...")
