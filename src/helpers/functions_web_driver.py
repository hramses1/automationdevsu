from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

def wait_visibility_element(driver, time_wait: int, common_by: str, locate_elements: str) -> WebElement | None:
    """
    Espera la visibilidad de un elemento localizado por un método específico (como ID, XPATH, etc.).

    Parámetros:
        - driver: El controlador de Selenium WebDriver.
        - time_wait: Tiempo máximo a esperar (en segundos).
        - common_by: Método de localización (ID, XPATH, CSS_SELECTOR, etc.).
        - locate_elements: Valor del localizador (ejemplo: "form_autocomplete_input").

    Retorna:
        - El WebElement encontrado o None si no se encuentra en el tiempo especificado.
    """
    attributes_by = getattr(By, common_by)  # Obtiene el método de localización de 'By'
    wait = WebDriverWait(driver, time_wait)  # Configura la espera explícita

    try:
        # Espera hasta que el elemento sea visible en la página
        element = wait.until(
            EC.visibility_of_element_located((attributes_by, locate_elements))
        )
        return element
    except TimeoutException:
        # Retorna None si el elemento no se encuentra visible dentro del tiempo de espera
        return None

def wait_present_element(driver, time_wait, common_by, locate_elements)-> WebElement | None:
    attributes_by = getattr(By, common_by)
    wait = WebDriverWait(driver, time_wait)
    try:
        element = wait.until(
            EC.presence_of_element_located((attributes_by, locate_elements))
        )
        return element
    except TimeoutException:
        return None
    
def wait_not_present_element(driver, time_wait, common_by, locate_elements)-> WebElement | None:
    attributes_by = getattr(By, common_by)
    wait = WebDriverWait(driver, time_wait)
    try:
        element = wait.until_not(
            EC.presence_of_element_located((attributes_by, locate_elements))
        )
        return element
    except TimeoutException:
        return None
    
def wait_clickable_element(driver, time_wait, common_by, locate_elements)-> WebElement | None:
    attributes_by = getattr(By, common_by)
    wait = WebDriverWait(driver, time_wait)
    try:
        element = wait.until(
            EC.element_to_be_clickable((attributes_by, locate_elements))
        )
        return element
    except TimeoutException:
        return None

def switch_to_frame(driver, time_wait, common_by, locate_elements):
    """
    Intenta cambiar al frame especificado y retorna un booleano indicando el éxito.
    
    :param driver: Instancia del navegador
    :param time_wait: Tiempo máximo en segundos para esperar que el frame esté disponible
    :param common_by: Método para localizar el elemento (ID, NAME, XPATH, etc.)
    :param locate_elements: Localizador del frame
    :return: bool - True si el cambio al frame fue exitoso, False de lo contrario
    """
    attributes_by = getattr(By, common_by)
    wait = WebDriverWait(driver, time_wait)
    try:
        wait.until(
            EC.frame_to_be_available_and_switch_to_it((attributes_by, locate_elements))
        )
        return True
    except TimeoutException:
        return False
def wait_and_accept_alert(driver, time_wait: int = 5) -> bool:
    """
    Espera la aparición de una alerta del navegador y la acepta.

    :param driver: Instancia del WebDriver
    :param time_wait: Tiempo máximo de espera en segundos
    :return: True si se aceptó la alerta, False si no apareció
    """
    try:
        WebDriverWait(driver, time_wait).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Texto de la alerta:", alert.text)
        alert.accept()
        return True
    except (TimeoutException, NoAlertPresentException):
        return False