import time
from selenium.webdriver.common.by import By


def test_language(browser, language):
    browser.get(f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    time.sleep(60)
    # во время паузы запустите pytest --language=fr test_items.py
    # в новом окне терминала на кнопке должна быть надпись "Ajouter au panier"
    button_chart = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button_chart.accessible_name == 'Añadir al carrito', 'worng language!'
    time.sleep(2)
