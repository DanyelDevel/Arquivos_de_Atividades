from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
navegador.get("https://bet7k.com/casino/13697-footballstudio")

email = "danyelhdss@gmail.com"
senha = "Dks.3211"

Botton_enter = navegador.find_element("xpath", '//*[@id="menu-horizontal"]/div[2]/div/div[2]/div/button[2]').click()
endereco = navegador.find_element("xpath", '//*[@id="email"]').send_keys(email)
senha = navegador.find_element('xpath', '//*[@id="password"]').send_keys(senha)
login = navegador.find_element('xpath', '//*[@id="login"]/div/div[2]/div/form/button').click()
sleep(15)

jogadas = navegador.find_element('xpath', 'evolutionSharedFrame').get_attribute()

