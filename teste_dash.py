import pytest
import time
from selenium import webdriver

chrome_path = '/home/lucasa/auto_python_pipeline/chrome-linux64/chrome'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)

url = 'http://127.0.0.1:8080'

#Teste da página inicial
driver.get(url)
time.sleep(10)
assert "Dash" in driver.title
assert "pagina inicial" in driver.page_source
print("Teste da pagina inicial realizado com sucesso!")

#Teste da página do formulário
driver.get(url+ "/formulario")
time.sleep(10)

assert "Dashboard - Formulario" in driver.title
assert "Formulario" in driver.page_source
print("Teste da pagina Formulario realizado com sucesso!")

#Teste da página de gráficos
driver.get(url+ "/graficos")
time.sleep(10)

assert "Dashboard - Graficos" in driver.title
assert "Graficos" in driver.page_source
print("Teste da pagina Graficos realizado com sucesso!")

driver.quit()