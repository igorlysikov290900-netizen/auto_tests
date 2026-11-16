import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderSamokatPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_field = OrderPageLocators.name_field
        self.surname_field = OrderPageLocators.surname_field
        self.adress_field = OrderPageLocators.adress
        self.metro_station_list = OrderPageLocators.metro_station_list
        self.metro_option = OrderPageLocators.metro_option
        self.phone_number_field = OrderPageLocators.phone_number
        self.next_button = OrderPageLocators.next_button
        self.date_field = OrderPageLocators.date_field
        self.date = OrderPageLocators.date
        self.rent_time = OrderPageLocators.rent_time
        self.rent_time_button = OrderPageLocators.rent_time_button
        self.collor = OrderPageLocators.collor
        self.order_button = OrderPageLocators.order_button
        self.accept_button = OrderPageLocators.accept_button
        self.accept_message = OrderPageLocators.accept_message
        self.status_button = OrderPageLocators.status_button
        self.samokat_button = OrderPageLocators.samokat_logo
        self.dzen_button = OrderPageLocators.dzen_button
        self.cookie_accept = OrderPageLocators.cookie_accept

    @allure.step('Принимаем куки')
    def click_cookie(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.cookie_accept)).click()

    @allure.step('Оформляем заказ')
    def order_samokat(self, name, surname, adress, phone):
        self.send_text(self.name_field, name)
        self.send_text(self.surname_field, surname)
        self.send_text(self.adress_field, adress)
        self.click_button(self.metro_station_list)
        self.click_button(self.metro_option)
        self.send_text(self.phone_number_field, phone)
        self.click_button(self.next_button)
        self.click_button(self.date_field)
        self.click_button(self.rent_time)
        self.click_button(self.rent_time_button)
        self.click_button(self.collor)
        self.click_button(self.order_button)
        self.click_button(self.accept_button)

    @allure.step('Кликаем по кнопке статуса заказа')
    def click_status_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.status_button)).click()

    @allure.step('Получаем ссылку логотипа самоката')
    def click_samokat_logo(self):
        self.click_button(self.samokat_button)
        current_link = self.driver.current_url
        return current_link
    
    @allure.step('Получаем ссылку логотипа яндекса')
    def click_dzen(self):
        self.click_button(self.dzen_button)
        current_link = self.driver.current_url
        return current_link