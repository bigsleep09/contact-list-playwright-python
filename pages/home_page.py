import allure
import pytest
from playwright.sync_api import Page, expect

from locators.contact_list_locators import HomePageLocators
from pages.contact_list_page import ContactListPage
from utils.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Input email: {email}")
    def _input_email(self, email: str):
        try:
            self.page.locator(HomePageLocators.email_input).press_sequentially(email, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting email: {email}. {str(e)}")

    @allure.step("Input password")
    def _input_password(self, password: str):
        try:
            self.page.locator(HomePageLocators.password_input).press_sequentially(password, timeout=200)
        except Exception as e:
            raise Exception(f"Error inputting password. {str(e)}")

    @allure.step("Click on submit button")
    def _click_submit(self):
        try:
            self.page.locator(HomePageLocators.submit_button).click()
        except Exception as e:
            raise Exception(f"Error clicking submit button. {str(e)}")

    @allure.step("Login with credentials: email={email}, password={password}")
    def login_with_credential(self, email: str, password: str)-> ContactListPage:
        try:
            self._input_email(email)
            self._input_password(password)
            self._click_submit()
            return ContactListPage(self.page)
        except Exception as e:
            raise Exception(f"Login failed for email: {email}. {str(e)}")


    def click_sign_in(self):
        try:
            self.page.click(HomePageLocators.sign_in_button)
        except Exception as e:
            self._attach_screenshot("Failed to click sign in button")
            raise Exception(f"Error clicking sign in button. {str(e)}")