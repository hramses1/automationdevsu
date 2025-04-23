import pytest
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

@pytest.fixture()
def init_driver(request):
    # Configuración de las opciones del navegador
    options = Options()
    #options.add_argument("--headless") #sin interfaz
    options.add_argument("--disable-gpu") # Desactiva la aceleración de GPU
    options.add_argument("--no-sandbox") # Desactiva las características de seguridad de aislamiento
    options.add_argument("--disable-dev-shm-usage") # Se usa para evitar que el navegador utilice la memoria compartida
    options.add_argument("--disable-resize")  # Deshabilita el ajuste del tamaño de la ventana
    options.add_argument("--disable-infobars")  # Deshabilita las barras de información (en caso de ser necesarias)
    options.add_argument("--start-maximized")  # Abre la ventana maximizada
    load_dotenv()
    # Inicialización del controlador de Selenium
    driver = WebDriver(options=options)
    driver.implicitly_wait(2) 
    #driver = webdriver.Remote(command_executor='http://chrome_selenium:4444/wd/hub', options=options)
    driver.get(os.getenv('URL'))
    
    # Asigna el controlador a la clase de la solicitud (request.cls) para que esté disponible en los métodos de la prueba
    request.cls.driver = driver

    # Ejecutar las pruebas
    yield 

    # Cerrar el controlador después de las pruebas
    driver.quit()