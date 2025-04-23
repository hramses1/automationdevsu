from src.helpers.functions_web_driver import wait_present_element,wait_and_accept_alert

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.__order1 = "Samsung galaxy s6"
        self.__bt_add_cart = "Add to cart"
        self.__order2 = "Nexus 6"
        self.__wait = 10
        
    def select_order_one(self):
        wait_present_element(self.driver,self.__wait, "LINK_TEXT", self.__order1).click()

    def select_buttom_add_cart(self):
        wait_present_element(self.driver,self.__wait, "LINK_TEXT", self.__bt_add_cart).click()
    
    def select_order_two(self):
        wait_present_element(self.driver,self.__wait, "LINK_TEXT", self.__order2).click()
    
    def back_page(self):
        self.driver.back()
        wait_and_accept_alert(self.driver)
        self.driver.back()