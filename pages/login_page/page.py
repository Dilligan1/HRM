import allure
from base.base_page import BasePage
from config.urls import Urls
from config.credentials import Credentials
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class LoginPage(BasePage):
    _PAGE_URL = Urls.LOGIN_PAGE


    _LOGIN_BUTTON = "//input[@type='submit']"
    _LOGIN_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"

    @allure.step("Login as {user_type}")
    def login_as(self, user_type):
        """
        :param user_type: Принимает в себя роль пользователя
        :return: None
        """
        import time
        # Очищаем поля (на странице могут быть значения по умолчанию)
        self.ui.fill(self._LOGIN_FIELD, "")
        self.ui.fill(self._PASSWORD_FIELD, "")

        if user_type == "admin":
            self.ui.fill(self._LOGIN_FIELD, Credentials.ADMIN_LOGIN)
            self.ui.fill(self._PASSWORD_FIELD, Credentials.ADMIN_PASSWORD)
            self.ui.click(self._LOGIN_BUTTON, "Login button")
        elif user_type == "friend":
            self.ui.fill(self._LOGIN_FIELD, Credentials.FRIEND_LOGIN)
            self.ui.fill(self._PASSWORD_FIELD, Credentials.FRIEND_PASSWORD)
            self.ui.click(self._LOGIN_BUTTON, "Login button")

        # Ждём загрузки страницы после логина
        time.sleep(3)
        self.wait.until(lambda d: d.current_url != Urls.LOGIN_PAGE)
        
        # Ждём появления главного элемента меню (гарантия загрузки страницы)
        from selenium.webdriver.common.by import By
        links_menu = (By.XPATH, "//a[text()='Links']")
        self.wait.until(EC.presence_of_element_located(links_menu))


