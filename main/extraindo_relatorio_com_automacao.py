from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt
import time
import pyautogui
import csv
import json
import os
import pandas as pd
import math


caminho_usuario = os.environ['USERPROFILE']
file_path = 'chamados.csv'
local_arquivo = os.path.join(caminho_usuario, "Downloads", file_path)
local_destino = os.path.join(caminho_usuario, 'ARQUIVOS', 'INTRANET')

# Apagando os arquivos anteriores existentes
if os.path.exists(local_arquivo):
    os.remove(local_arquivo)

# Configurar as opções do navegador Chrome
options = Options()
options.add_argument("--disable-notifications")  # Desabilitar notificações, se necessário

# Inicializar o navegador Chrome com as opções configuradas e o ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Acessar o site
driver.get('https://intranet.solidy.org.br/intranet/login')

# Localizar o campo de entrada de e-mail pelo caminho completo fornecido
email_input = driver.find_element(
    'xpath', '/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/form/div[1]/input'
)

# Limpar o campo de e-mail (opcional)
email_input.clear()

# Digitar o e-mail desejado
email_input.send_keys('{E-MAIL}')

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
senha_input.send_keys('{SENHA}')

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

# pyautogui.alert('Relatório baixado')

# Leia o arquivo CSV
# with open('C:\\Users\\Solidy-TI\\Downloads\\chamados.csv', mode='r', encoding='utf-8') as csvfile:

arquivo = True

while arquivo == True:
    if os.path.exists(local_arquivo):
        dfu = pd.read_csv(f"{local_arquivo}",
                          skiprows=0,
                          sep=";",
                          encoding="UTF-8"
                          )
        # Fechar o navegador
        driver.quit()
        arquivo = False
    else:
        # Aguarda 5 segundos
        time.sleep(5)

# Renomeando as colunas
dfu = dfu.rename(columns={"Código":"id_chamado",
                          "Assunto":"assunto",
                          "Contato":"contato",
                          "Email do Contato":"email_do_contato",
                          "Unidade":"unidade",
                          "Departamento":"departamento",
                          "Cargo":"cargo",
                          "Tipo":"tipo",
                          "Situação":"situacao",
                          "Atendente":"atendente",
                          "Grupo":"grupo",
                          "Prioridade":"prioridade",
                          "Criado Em": "criado_em",
                          "Prazo da primeira resposta": "prazo_da_primeira_resposta",
                          "Primeira resposta":"primeira_resposta",
                          "Prazo de resolução":"prazo_de_resolucao",
                          "Concluído Em":"concluído_em",
                          "Ultima alteração":"ultima_alteracao",
                          "SLA":"sla",
                          "Primeira atribuição em":"primeira_atribuicao_em"
                          })


# Lista de colunas de data para formatar
colunas_data = [
    "criado_em",
    "prazo_da_primeira_resposta",
    "primeira_resposta",
    "prazo_de_resolucao",
    "concluído_em",
    "ultima_alteracao",
    "primeira_atribuicao_em"
]

# Converter todas as colunas de data para o formato correto
for coluna in colunas_data:
    dfu[coluna] = pd.to_datetime(dfu[coluna], format="%d/%m/%Y %H:%M").dt.strftime("%Y-%m-%d %H:%M")


nome_saida = os.path.join(local_destino, f"chamados.csv")
nome_saida2 = os.path.join(local_destino, f"chamados.json")
dados = dfu.to_dict(orient='records')


# Modificando os valores de NONE para NULL
for dict in dados:
    for chave, valor in dict.items():
        if isinstance(valor, float) and math.isnan(valor):
            dict[chave] = None



if os.path.exists(nome_saida):
    os.remove(nome_saida)
    dfu.to_csv(nome_saida,
               header=True,
               index=False,
               sep=";",
               encoding="UTF-8"
               )

else:
    dfu.to_csv(nome_saida,
               header=True,
               index=False,
               sep=";",
               encoding="UTF-8"
               )

if os.path.exists(nome_saida2):
    os.remove(nome_saida2)
    with open(nome_saida2, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

else:
    with open(nome_saida2, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

