import random
from faker import Faker


class FakeData:

    def __init__(self, locale='es_ES'):
        """
        Inicializa el generador de datos falsos para el formulario 'Place order'.
        """
        self.fake = Faker(locale)
        self.country_city_map = {
            "Argentina": ["Buenos Aires"],
            "Brazil": ["São Paulo"],
            "Chile": ["Santiago"],
            "Colombia": ["Bogotá"],
            "Costa Rica": ["San José"],
            "Cuba": ["La Habana"],
            "Ecuador": ["Guayaquil"],
            "El Salvador": ["San Salvador"],
            "Spain": ["Madrid", "Barcelona"],
            "Mexico": ["Ciudad de México"],
            "Panama": ["Ciudad de Panamá"],
            "Paraguay": ["Asunción"],
            "Peru": ["Lima"],
            "Portugal": ["Lisboa"],
            "Uruguay": ["Montevideo"],
            "Venezuela": ["Caracas"]
        }

    def get_country(self):
        """Devuelve un país aleatorio del mapa."""
        return random.choice(list(self.country_city_map.keys()))

    def get_city(self, country):
        """Devuelve una ciudad válida correspondiente al país."""
        return random.choice(self.country_city_map[country])

    def get_name(self):
        """Genera un nombre completo aleatorio."""
        return f"{self.fake.first_name()} {self.fake.last_name()}"

    def get_credit_card_number(self):
        """Genera un número de tarjeta de crédito válido."""
        return self.fake.credit_card_number()

    def get_credit_card_month(self):
        """Devuelve el mes de expiración de la tarjeta (MM)."""
        return self.fake.credit_card_expire().split('/')[0]

    def get_credit_card_year(self):
        """Devuelve el año de expiración de la tarjeta (YY o YYYY)."""
        return self.fake.credit_card_expire().split('/')[1]
