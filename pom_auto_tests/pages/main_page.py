import allure
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получаем текст вопроса")
    def get_question_text(self, button, text):
        self.scroll_and_click(button)
        return self.get_text(text)