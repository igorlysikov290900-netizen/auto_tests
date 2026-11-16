import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# класс страницы авторизации
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку')
    def click_button(self, button):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(button)).click()

    @allure.step('Заполняем поле')
    def send_text(self, locator, text):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)
    
    @allure.step('Получаем текст')
    def get_text(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text


    @allure.step('Прокручиваем и кликаем')
    def scroll_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
