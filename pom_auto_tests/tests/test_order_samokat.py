import allure
import pytest
import random as r
from data import TestData, Urls
from pages.order_samokat_page import OrderSamokatPage
from locators.order_page_locators import OrderPageLocators

@allure.title('Проверка оформления заказа')
@allure.description('На базовой странице ищем элемент заказа, вносим все необходимые наборы данных, оформляем заказ и проверяем ссылки в шапке страницы')
class TestOrderSamokat:
    
    @pytest.mark.parametrize('name,surname,adress,buttons', list(zip(TestData.names, TestData.surnames, TestData.adresses, TestData.buttons)))
    def test_order(self, driver, name, surname, adress, buttons):
        phone = str(r.randint(10000000000, 99999999999))
        page = OrderSamokatPage(driver)
        page.click_cookie()
        page.click_button(buttons)
        page.order_samokat(name, surname, adress, phone)
        assert "Заказ оформлен" in driver.find_element(*OrderPageLocators.accept_message).text
        page.click_status_button()
        current_link = page.click_samokat_logo()
        assert current_link == Urls.expected_samokat_url
        current_link = page.click_dzen()
        assert current_link == Urls.expected_dzen_url