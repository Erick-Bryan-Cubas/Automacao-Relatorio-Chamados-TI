# Automação com a biblioteca Selenium

Este é um exemplo de código Python que utiliza a biblioteca Selenium para automatizar a navegação em um site, preencher campos de e-mail e senha, clicar em botões e acessar menus. O código também inclui a biblioteca PyAutoGUI para simular pressionamentos de teclas e cliques do mouse.

## Instruções

Antes de executar o código, substitua as seguintes variáveis:

- `{ENDEREÇO INTRANET}`: O URL do site que você deseja acessar.
- `{EMAIL}`: O endereço de e-mail que deseja inserir no campo de e-mail.
- `{SENHA}`: A senha que deseja inserir no campo de senha.

### Passo a passo do código

1. Configurar as opções do navegador Chrome, desabilitando notificações (opcional).
2. Inicializar o navegador Chrome com as opções configuradas e o ChromeDriverManager.
3. Acessar o site usando o método `get()`.
4. Localizar e preencher os campos de e-mail e senha usando o método `find_element()`.
5. Simular pressionar a tecla Enter para enviar os campos de e-mail e senha.
6. Aguardar 5 segundos para garantir que as ações sejam concluídas.
7. Navegar até o menu e clicar nele.
8. Acessar o menu "Help Desk" e clicar nele.
9. Acessar o menu "Intra Produtividade" e clicar nele.
10. Fechar o navegador após concluir as ações.
11. Exibir um alerta com a mensagem "Relatório baixado" ao finalizar o processo.

## Referências

- [Selenium](https://www.selenium.dev/)
- [WebDriverManager](https://github.com/webdriver-manager/webdriver-manager)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) 