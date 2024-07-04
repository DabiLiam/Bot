import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Função para executar as ações repetitivas
def executar_tarefa(navegador, x, y, incremento_y, iteracao):
    # Abrir a ferramenta/o sistema/o programa
    pyautogui.press('win')
    pyautogui.write('Nome do Arquivo...')
    pyautogui.press('enter')

    # Pegar id
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()
    time.sleep(0.8)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)


    # Condicional para mudar comportamento
    
    caixa_de_pesquisa = navegador.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/span[2]/div/div[1]/div/div/input')
    caixa_de_pesquisa.clear()
    time.sleep(2)
    caixa_de_pesquisa.click()
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2.4)
    pyautogui.moveTo(x=0, y=0)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/a/div[2]/div/div[5]/div/div[1]/button').click()
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]').click()
    time.sleep(2)

    # Incrementar y para a próxima repetição
    y += incremento_y
    return y

# Configuração inicial
pyautogui.PAUSE = 2
navegador = webdriver.Chrome()

# Maximizar a janela do navegador para tela cheia
navegador.maximize_window()

# Abrir a página de login da Shopee
navegador.get('https://shopee.com.br/seller/login')
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/form/div[1]/div[1]/input').send_keys('')
navegador.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[1]/input').send_keys('')
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/form/button').click()
time.sleep(5)

# Navegar e realizar ações no navegador
navegador.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div[1]/div/div').click()
time.sleep(4)
navegador.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div').click()
time.sleep(3)
navegador.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div[1]/div[5]/div/div[1]/div/span').click()

# Coordenadas iniciais
x = 77
y = 278
incremento_y = 30  # Valor para incrementar o y a cada repetição

# Número de repetições
numero_de_repeticoes = 5

# Loop para repetir o processo
for iteracao in range(numero_de_repeticoes):
    y = executar_tarefa(navegador, x, y, incremento_y, iteracao)

# Manter o navegador aberto após as repetições
input("Pressione Enter para encerrar o script e fechar o navegador...")
navegador.quit()
