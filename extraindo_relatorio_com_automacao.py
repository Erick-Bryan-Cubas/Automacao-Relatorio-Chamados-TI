from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

# Configurar as opções do navegador Chrome
options = Options()
options.add_argument("--disable-notifications")  # Desabilitar notificações, se necessário

# Inicializar o navegador Chrome com as opções configuradas e o ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Acessar o site
driver.get('{ENDEREÇO INTRANET}')

# Localizar o campo de entrada de e-mail pelo caminho completo fornecido
email_input = driver.find_element(
    'xpath', '/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/form/div[1]/input'
)

# Limpar o campo de e-mail (opcional)
email_input.clear()

# Digitar o e-mail desejado
email_input.send_keys('{EMAIL}')

# Simular pressionar a tecla Enter
email_input.send_keys(Keys.ENTER)

time.sleep(5)  # Aguarda 5 segundos


# Digitar a senha
senha_input = driver.find_element(
    'xpath', '/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/form/div[1]/input'
)

# Limpar o campo de senha (opcional)
senha_input.clear()

# Digitar a senha
senha_input.send_keys('[SENHA}')

time.sleep(2)  # Aguarda 5 segundos


# Localizar o botão "Acessar" pelo caminho completo fornecido
acessar_button = driver.find_element(
    'xpath', '//*[@id="user-login"]/div[3]/div[2]/button'
)

# Clicar no botão "Acessar"
acessar_button.click()

time.sleep(10)  # Aguarda 5 segundos

# Localizar o menu pelo caminho completo fornecido
menu_button = driver.find_element(
    'xpath', '//*[@id="header-col-user-link-menu"]'
)

# Clicar no menu
menu_button.click()

time.sleep(2)  # Aguarda 2 segundos

# Localizar o item do menu pelo caminho completo fornecido
item_menu = driver.find_element(
    'xpath', '//*[@id="header"]/div/div[4]/div/div[2]/ul/li[6]/a'
)

# Clicar no item do menu
item_menu.click()

time.sleep(5)  # Aguarda 5 segundos

# Digitar a senha para acessar o painel administrador
senha_input = driver.find_element(
    'xpath', '//*[@id="intranet-login"]/form/input'
)

# Limpar o campo de senha (opcional)
senha_input.clear()

# Digitar a senha
senha_input.send_keys('{SENHA}')

time.sleep(2)  # Aguarda 5 segundos

# Localizar o botão "Confirmar senha" pelo caminho completo fornecido
acessar_button = driver.find_element(
    'xpath', '//*[@id="intranet-login"]/form/button'
)

# Clicar no botão "Acessar"
acessar_button.click()

time.sleep(5)  # Aguarda 5 segundos

# Localizar o botão "Intra Produtividade" pelo caminho completo fornecido
acessar_button = driver.find_element(
    'xpath', '//html/body/nav/div[1]/div[1]/a[2]'
)

# Clicar no botão "Acessar"
acessar_button.click()

time.sleep(10)  # Aguarda 5 segundos

# Localizar o botão "Help Desk" pelo caminho completo fornecido
acessar_button = driver.find_element(
    'xpath', '//*[@id="body-content"]/div[2]/div[2]/div/div[2]/div/div[8]'
)

# Clicar no botão "Acessar"
acessar_button.click()

time.sleep(10)  # Aguarda 5 segundos


# Localizar o botão "Help Desk" pelo caminho completo fornecido
acessar_button = driver.find_element(
    'xpath', '//*[@id="body-content"]/div[2]/div[1]/div[1]/div[2]/ul/li[2]/a'
)

# Clicar no botão "Acessar"
acessar_button.click()

time.sleep(10)  # Aguarda 5 segundos


# Fechar o navegador
driver.quit()
pyautogui.alert('Relatório baixado')