from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://bet7k.com/casino/13697-footballstudio')

email = "danyelhdss@gmail.com"
senha = "Dks.3211"

Botão_entra = driver.find_element('xpath' , '//*[@id="menu-horizontal"]/div[2]/div/div[2]/div/button[2]').click()
Login = driver.find_element('xpath' , '//*[@id="email"]').send_keys(email)
Senha = driver.find_element('xpath' , '//*[@id="password"]').send_keys(senha)
Senha = driver.find_element('xpath' , '//*[@id="login"]/div/div[2]/div/form/button').click()

while len(driver.find_elements(By.XPATH, '//*[@id="chat-widget"]')) -- 0:
    time.sleep(2)

idroot = driver.find_element(By.XPATH, '//*[@id="chat-widget"]')

driver.switch_toid(id)

while len(driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div/div[2]')) --0:
    time.sleep(2)

elemento = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div/div[2]').text

print(elemento)

# botão de janela flutuante //*[@id="deposit-modal___BV_modal_header_"]/button
