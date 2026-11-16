from locators.main_page_locators import MainPageLocators

class TestData:

    names = ['Игорь', 'Игорян']
    surnames = ['Лысиков', 'Лысикян']
    addresses = ['Пушкина', 'Колотушкина']
    buttons = [MainPageLocators.order_button_upper_menu, MainPageLocators.order_button_page_down]

class Urls:
    expected_samokat_url = "https://qa-scooter.education-services.ru/"
    expected_dzen_url = "https://dzen.ru/"