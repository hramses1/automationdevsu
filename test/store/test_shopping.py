import time
import pytest
from src.store.order.order_page import OrderPage
from src.store.carShop.car_shop_page import CarShopPage
from src.common.fakeData.fake_data_page import FakeData

@pytest.mark.usefixtures("init_driver")
class TestShopping:

    def test_order_product(self):
        
        desk_page = OrderPage(self.driver)
        cart_page = CarShopPage(self.driver)
        data = FakeData()

        # Agregar primer producto
        desk_page.select_order_one()
        desk_page.select_buttom_add_cart()
        desk_page.back_page()

        # Agregar segundo producto
        desk_page.select_order_two()
        desk_page.select_buttom_add_cart()
        desk_page.back_page()

        # Ir al carrito
        cart_page.click_cart_button()

        # Hacer clic en "Place Order"
        cart_page.click_place_order_button()

        # Llenar el formulario con datos
        country = data.get_country()
        cart_page.fill_order_form(
            name=data.get_name(),
            country=country,
            city=data.get_city(country),
            card=data.get_credit_card_number(),
            month=data.get_credit_card_month(),
            year=data.get_credit_card_year()
        )
        cart_page.click_purchase_button()
        cart_page.click_confirm_button()
        
        assert cart_page.get_confirmation_text() == "Thank you for your purchase!"


