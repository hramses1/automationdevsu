# 🛒 Automation Devsu - E2E Shopping Flow with Selenium & Pytest

Este proyecto automatiza un flujo completo de compra en un entorno web simulado, utilizando **Selenium** como motor de automatización, junto con **Pytest** como framework de pruebas. Está organizado bajo el patrón **Page Object Model (POM)**

## 📁 Estructura del proyecto

```
automationdevsu/
├── src/
│   ├── common/
│   │   └── fakeData/
│   │       └── fake_data_page.py         # Generador de datos falsos personalizados
│   ├── data/                             # (Reservado para fixtures/datasets)
│   ├── helpers/
│   │   └── functions_web_driver.py       # Funciones utilitarias para WebDriver
│   └── store/
│       ├── carShop/
│       │   └── car_shop_page.py          # PageObject del carrito y formulario
│       └── order/
│           └── order_page.py             # PageObject para seleccionar productos
├── test/
│   └── store/
│       └── test_shopping.py              # Test principal: flujo de compra
├── .env                                  # Variables de entorno (URL, etc.)
├── .env.example                          # Plantilla para variables de entorno
├── .gitignore                            # Archivos y carpetas ignoradas por git
├── conftest.py                           # Configuración global para Pytest
├── requirements.txt                      # Dependencias del proyecto
└── README.md                             # Este archivo
```

## 🚀 ¿Qué hace este proyecto?

1. Abre el navegador.
2. Ingresa a la tienda online definida en la variable `URL` (en `.env`).
3. Selecciona productos del catálogo.
4. Agrega productos al carrito.
5. Procede al checkout.
6. Rellena el formulario con datos generados automáticamente.
7. Finaliza la compra y verifica el mensaje de confirmación.

## ⚙️ Requisitos

- Python 3.10 o superior
- Google Chrome
- ChromeDriver compatible
- Virtualenv (opcional pero recomendado)

## 🧪 Ejecución de pruebas

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Crea un archivo `.env` (puedes copiar `.env.example`) y define al menos:

```
URL=https://tutienda.com
```

Ejecuta el test principal:

```bash
pytest -v test/store/test_shopping.py
```
Generar reporte:

```bash
pytest --html=reports/report.html
```


## 📌 Notas

- Los datos del formulario (`name`, `country`, `city`, etc.) son generados dinámicamente usando Faker.
- La estructura POM permite agregar o modificar páginas fácilmente sin afectar los tests existentes.
