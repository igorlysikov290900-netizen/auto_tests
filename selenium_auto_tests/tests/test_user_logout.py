from helpers import click_button, send_keys, get_text, is_element_visible
from locators.locators import LoginLocators



class TestUserLogout:

    def test_user_logout(self, driver):
        email = 'name1234@gmail.com'
        password = 'password'
        click_button(driver, LoginLocators.login_window_button)
        send_keys(driver, LoginLocators.email_field, email)
        send_keys(driver, LoginLocators.password_field, password)
        click_button(driver, LoginLocators.login_button)
        click_button(driver, LoginLocators.logout_button)
        assert get_text(driver, LoginLocators.add_ad_button) == 'Разместить объявление' 
        assert get_text(driver, LoginLocators.login_window_button) == 'Вход и регистрация' 
        assert is_element_visible(driver, LoginLocators.user_name) == False 
        assert is_element_visible(driver, LoginLocators.user_logo) == False
