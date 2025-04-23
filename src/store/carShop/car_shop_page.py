from src.helpers.functions_web_driver import (
    wait_present_element,
    wait_and_accept_alert,
    wait_clickable_element
)

class CarShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.__btn_cart = "cartur"
        self.__btn_purchase = "#orderModal .btn-primary"
        self.__btn_place_order = ".btn-success"
        self.__btn_confirm = ".confirm"
        self.__txt_confirm = "h2:nth-child(6)"
        self.__wait = 10

        # IDs del formulario
        self.__input_name = "name"
        self.__input_country = "country"
        self.__input_city = "city"
        self.__input_card = "card"
        self.__input_month = "month"
        self.__input_year = "year"


    def click_cart_button(self):
        wait_present_element(self.driver, self.__wait, "ID", self.__btn_cart).click()

    def click_place_order_button(self):
        wait_clickable_element(self.driver, self.__wait, "CSS_SELECTOR", self.__btn_place_order).click()
    
    def click_purchase_button(self):
        wait_present_element(self.driver, self.__wait, "CSS_SELECTOR", self.__btn_purchase).click()
    
    def click_confirm_button(self):
        wait_present_element(self.driver, self.__wait, "CSS_SELECTOR", self.__btn_confirm).click()
        
    def is_confirmation_displayed(self):
        element = wait_present_element(self.driver, self.__wait, "CSS_SELECTOR", self.__txt_confirm)
        return element.is_displayed() if element else False
    
    def get_confirmation_text(self):
        element = wait_present_element(self.driver, self.__wait, "CSS_SELECTOR", self.__txt_confirm)
        return element.text.strip() if element else None

    def fill_name(self, name):
        wait_present_element(self.driver, self.__wait, "ID", self.__input_name).send_keys(name)

    def fill_country(self, country):
        wait_present_element(self.driver, self.__wait, "ID", self.__input_country).send_keys(country)

    def fill_city(self, city):
        wait_present_element(self.driver, self.__wait, "ID", self.__input_city).send_keys(city)

    def fill_credit_card(self, card_number):
        wait_present_element(self.driver, self.__wait, "ID", self.__input_card).send_keys(card_number)

    def fill_month(self, month):
        wait_present_element(self.driver, self.__wait, "ID", self.__input_month).send_keys(month)

    def fill_year(self, year):
        wait_present_element(self.driver, self.__wait, "ID", self.__input_year).send_keys(year)

    def fill_order_form(self, name, country, city, card, month, year):
        self.fill_name(name)
        self.fill_country(country)
        self.fill_city(city)
        self.fill_credit_card(card)
        self.fill_month(month)
        self.fill_year(year)

    def back_page(self):
        self.driver.back()
        wait_and_accept_alert(self.driver)
        self.driver.back()
